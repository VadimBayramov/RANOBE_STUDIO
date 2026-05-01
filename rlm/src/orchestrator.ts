import Anthropic from "@anthropic-ai/sdk";
import type { Corpus, RLMConfig, RunResult } from "./types.js";
import { ReplClient } from "./repl.js";
import { criticAgent } from "./critic.js";
import { corpusSummary } from "./corpus.js";

export type RLMStage = "kb" | "facts" | "general";

const EXEC_REPL_TOOL: Anthropic.Messages.Tool = {
  name: "exec_repl",
  description:
    "Execute Python code in a persistent REPL. Variables survive between calls. " +
    "stdout is truncated to 800 chars — store intermediate results in variables, not in print(). " +
    "End the session by calling print(FINAL('your complete answer')).",
  input_schema: {
    type: "object" as const,
    properties: {
      code: {
        type: "string",
        description:
          "Python code. Namespace: chunks (list[{id,source,text}]), " +
          "search(pattern, max_hits=20) → list[{id,source,preview}], " +
          "sub_rlm(chunk_id, question) → str, re, json.",
      },
    },
    required: ["code"],
  },
};

// KB stage: corpus = 0. LIBRARY/studies/ — knowledge cards with frontmatter
const KB_SYSTEM_SUFFIX = `
The corpus consists of RANOBE_STUDIO knowledge-base cards. Each card has YAML frontmatter:
  card_id: NRO-042          (prefix = domain code)
  domain: neuroscience|psychology|narratology|style|characters|worldbuilding|
          structure|emotions|sociology|combat|genre|cultivation|mythology|
          tactics|cinema|culture
  stage: [idea|bible|chapter]   (pipeline stage where this card applies)
  scene_type: [arc_design|emotional_beat|combat|dialogue|introspection|...]
  tags: [...]
  confidence: high|medium|low

Card body sections (in Russian):
  ## Принцип        — one-sentence core technique
  ## Из исследования — scientific/source basis
  ## Как применить в ранобэ — concrete application to writing
  ## Пример ✓       — good example in ranobe style
  ## Пример ✗       — what NOT to do

Search strategy for KB:
- Use domain codes in regex: search('NRO|PSY') to filter by domain
- Use tags/terms: search('cultivation|breakthrough|dao|heart_devil')
- Ask sub_rlm() with precise questions: 'What specific technique for [scene_type]?'
- Cross-domain synthesis is expected — one scene often needs CMB + PSY + EMO cards

Answer in Russian. Synthesize across domains. Quote card_id in your answer.`;

// Facts stage: corpus = 3. GENERATION/drafts/ — previously written chapters
const FACTS_SYSTEM_SUFFIX = `
The corpus consists of previously written chapters of the ranobe (light novel).
Files are named ch_NNN.md — each is one chapter.

Your task: find factual information from past chapters to answer the question.
- search() for character names, place names, events, objects
- sub_rlm() to extract the specific fact from the chunk
- Always cite the chapter number [ch_NNN] in your answer

Answer in Russian.`;

function buildSystemPrompt(corpus: Corpus, stage: RLMStage): string {
  const base = `You are an Algorithm 1 RLM orchestrator for RANOBE_STUDIO — a writing platform for long-form Japanese-style light novels (ranobe).
Your task: answer the user's question about a large corpus that does not fit in context.

${corpusSummary(corpus)}

REPL namespace:
  chunks     — list[{id, source, text}], the full corpus
  search(pattern, max_hits=20) → list[{id, source, preview}]  (regex, case-insensitive)
  sub_rlm(chunk_id, question)  → "NOT_FOUND" | "1-4 sentence answer"  (leaf agent)
  re, json   — standard modules

Algorithm:
1. search() to discover candidate chunks.
2. sub_rlm() to extract signal from each candidate.
3. Store results in variables — stdout is truncated to 800 chars, variables are not.
4. print(FINAL("complete answer")) when done.

Rules:
- Write loops and conditionals. Do not call sub_rlm() one by one in separate exec_repl calls.
- Never print full chunk texts — they exceed the truncation limit.
- sub_rlm() for analysis. search() for discovery. Variables for memory.`;

  const suffix = stage === "kb"
    ? KB_SYSTEM_SUFFIX
    : stage === "facts"
    ? FACTS_SYSTEM_SUFFIX
    : "\n\nAnswer in Russian.";

  return base + suffix;
}

type Stats = {
  iterations: number;
  replCalls: number;
  criticCycles: number;
  totalInput: number;
  totalOutput: number;
  leafInput: number;
  leafOutput: number;
};

async function runREPLLoop(
  client: Anthropic,
  config: RLMConfig,
  corpus: Corpus,
  stage: RLMStage,
  repl: ReplClient,
  messages: Anthropic.Messages.MessageParam[],
  stats: Stats,
  log: (s: string) => void
): Promise<string | null> {
  for (let i = 0; i < config.maxIterations; i++) {
    stats.iterations++;
    log(`[iter ${stats.iterations}] thinking...`);

    const resp = await client.messages.create({
      model: config.orchestratorModel,
      max_tokens: 4096,
      system: buildSystemPrompt(corpus, stage),
      tools: [EXEC_REPL_TOOL],
      messages,
    });

    stats.totalInput += resp.usage.input_tokens;
    stats.totalOutput += resp.usage.output_tokens;
    messages.push({ role: "assistant", content: resp.content });

    if (resp.stop_reason === "end_turn") {
      const text = resp.content.find((b) => b.type === "text");
      return text?.type === "text" ? text.text.trim() : null;
    }

    if (resp.stop_reason !== "tool_use") return null;

    const toolBlocks = resp.content.filter(
      (b): b is Anthropic.Messages.ToolUseBlock => b.type === "tool_use"
    );

    const toolResults: Anthropic.Messages.ToolResultBlockParam[] = [];
    let finalAnswer: string | null = null;

    for (const block of toolBlocks) {
      if (block.name !== "exec_repl") continue;

      stats.replCalls++;
      const code = (block.input as { code: string }).code;
      log(`  → exec_repl (${code.split("\n").length} lines)`);

      const result = await repl.exec(code);
      stats.leafInput += result.leafInputTokens;
      stats.leafOutput += result.leafOutputTokens;

      if (result.error) log(`  ✗ error: ${result.error.slice(0, 160)}`);
      if (result.stdout) log(`  out: ${result.stdout.slice(0, 160)}`);
      if (result.final) {
        finalAnswer = result.final;
        log(`  → FINAL`);
      }

      toolResults.push({
        type: "tool_result",
        tool_use_id: block.id,
        content: result.error
          ? `${result.stdout}\nERROR:\n${result.error}`
          : result.stdout || "(no output)",
      });
    }

    messages.push({ role: "user", content: toolResults });

    if (finalAnswer) return finalAnswer;
  }

  return null;
}

export async function runRLM(
  client: Anthropic,
  config: RLMConfig,
  corpus: Corpus,
  question: string,
  stage: RLMStage = "general",
  onEvent?: (event: string) => void
): Promise<RunResult> {
  const log = (msg: string) => onEvent?.(msg);

  const repl = await ReplClient.create(client, config.leafModel, corpus);
  const messages: Anthropic.Messages.MessageParam[] = [{ role: "user", content: question }];
  const stats: Stats = {
    iterations: 0,
    replCalls: 0,
    criticCycles: 0,
    totalInput: 0,
    totalOutput: 0,
    leafInput: 0,
    leafOutput: 0,
  };

  try {
    let answer = await runREPLLoop(client, config, corpus, stage, repl, messages, stats, log);
    answer = answer ?? `(max ${config.maxIterations} iterations reached without FINAL)`;

    for (let c = 0; c < config.criticIterations; c++) {
      stats.criticCycles++;
      log(`[critic ${c + 1}/${config.criticIterations}] reviewing...`);

      const critique = await criticAgent(client, config.criticModel, question, answer);
      stats.totalInput += critique.inputTokens;
      stats.totalOutput += critique.outputTokens;
      log(`  → ${critique.verdict}`);

      if (critique.verdict === "APPROVED") break;

      messages.push({
        role: "user",
        content: `Critic feedback:\n${critique.feedback}\n\nYour previous answer:\n${answer}\n\nAddress the issues using exec_repl, then print(FINAL('improved answer')).`,
      });

      const refined = await runREPLLoop(client, config, corpus, stage, repl, messages, stats, log);
      if (refined) answer = refined;
    }

    return {
      answer,
      iterations: stats.iterations,
      criticCycles: stats.criticCycles,
      replCalls: stats.replCalls,
      totalInputTokens: stats.totalInput + stats.leafInput,
      totalOutputTokens: stats.totalOutput + stats.leafOutput,
    };
  } finally {
    repl.destroy();
  }
}
