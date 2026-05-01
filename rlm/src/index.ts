import "dotenv/config";
import { resolve, dirname } from "node:path";
import { fileURLToPath } from "node:url";
import Anthropic from "@anthropic-ai/sdk";
import { loadCorpus } from "./corpus.js";
import { runRLM, type RLMStage } from "./orchestrator.js";
import type { RLMConfig } from "./types.js";

const __dirname = dirname(fileURLToPath(import.meta.url));
// Default KB corpus: 0. LIBRARY/studies/ relative to repo root
const DEFAULT_KB_CORPUS = resolve(__dirname, "../../0. LIBRARY/studies");
// Default facts corpus: 3. GENERATION/drafts/ relative to repo root
const DEFAULT_FACTS_CORPUS = resolve(__dirname, "../../3. GENERATION/drafts");

type ParsedArgs = {
  corpusPath: string;
  question: string;
  verbose: boolean;
  critic: boolean;
  stage: RLMStage;
  json: boolean;
};

function parseArgs(argv: string[]): ParsedArgs {
  const args = argv.slice(2);
  let corpus = "";
  let question = "";
  let verbose = false;
  let critic = false;
  let stage: RLMStage = "general";
  let json = false;

  for (let i = 0; i < args.length; i++) {
    const a = args[i];
    if (a === "--corpus" || a === "-c") corpus = args[++i];
    else if (a === "--stage" || a === "-s") stage = args[++i] as RLMStage;
    else if (a === "--verbose" || a === "-v") verbose = true;
    else if (a === "--critic") critic = true;
    else if (a === "--json") json = true;
    else if (a === "--help" || a === "-h") { printHelp(); process.exit(0); }
    else if (!question) question = a;
    else question += " " + a;
  }

  // Resolve default corpus based on stage
  if (!corpus) {
    corpus = stage === "facts" ? DEFAULT_FACTS_CORPUS : DEFAULT_KB_CORPUS;
  }

  return { corpusPath: corpus, question, verbose, critic, stage, json };
}

function printHelp() {
  console.log(`ranobe-rlm — Algorithm 1 RLM for RANOBE_STUDIO (arxiv:2512.24601)

Usage:
  npm run ask -- "<question>" [--stage kb|facts|general] [--corpus <path>] [--verbose] [--critic] [--json]

Stages:
  kb      Query the knowledge base (0. LIBRARY/studies/) — craft techniques, card synthesis
  facts   Verify facts in written chapters (3. GENERATION/drafts/)
  general Custom corpus, no ranobe-specific context

Options:
  --corpus, -c   Override corpus path
  --stage, -s    Pipeline stage: kb | facts | general (default: general)
  --verbose, -v  Stream REPL events to stderr
  --critic       Enable critic loop (auto-refine answer)
  --json         Output result as JSON (for pipeline scripts)
  --help, -h     Show this help

Pipeline examples:
  # Scene plan: what techniques for a cultivation breakthrough scene?
  npm run ask -- "техники для сцены прорыва культивации под давлением врага" --stage kb

  # Bible: what do we know about reader engagement in the first 3 chapters?
  npm run ask -- "как удержать читателя в первых 3 главах xianxia" --stage kb --critic

  # Fact check: did Arkash visit the temple before?
  npm run ask -- "посещал ли Аркаш храм Ринтаро до главы 20" --stage facts

  # Cross-domain: complex emotional combat scene
  npm run ask -- "сцена боя где герой теряет учителя — как совместить CMB и EMO техники" --stage kb

Env (.env):
  ANTHROPIC_API_KEY=sk-ant-...
  RLM_ORCHESTRATOR_MODEL  (default: claude-sonnet-4-6)
  RLM_LEAF_MODEL          (default: claude-haiku-4-5-20251001)
  RLM_CRITIC_MODEL        (default: claude-haiku-4-5-20251001)
  RLM_MAX_ITERATIONS      (default: 20)
  RLM_CRITIC_ITERATIONS   (default: 3)
  RLM_CHUNK_CHARS         (default: 4000)
  RLM_CHUNK_OVERLAP       (default: 200)
`);
}

async function main() {
  const { corpusPath, question, verbose, critic, stage, json } = parseArgs(process.argv);

  if (!question) { printHelp(); process.exit(1); }

  if (!process.env.ANTHROPIC_API_KEY) {
    console.error("ERROR: ANTHROPIC_API_KEY missing. Copy .env.example to .env and fill it.");
    process.exit(1);
  }

  const config: RLMConfig = {
    orchestratorModel: process.env.RLM_ORCHESTRATOR_MODEL ?? "claude-sonnet-4-6",
    leafModel: process.env.RLM_LEAF_MODEL ?? "claude-haiku-4-5-20251001",
    criticModel: process.env.RLM_CRITIC_MODEL ?? "claude-haiku-4-5-20251001",
    maxIterations: Number(process.env.RLM_MAX_ITERATIONS ?? 20),
    criticIterations: critic ? Number(process.env.RLM_CRITIC_ITERATIONS ?? 3) : 0,
    chunkChars: Number(process.env.RLM_CHUNK_CHARS ?? 4000),
    chunkOverlap: Number(process.env.RLM_CHUNK_OVERLAP ?? 200),
  };

  console.error(`[rlm] stage=${stage} corpus=${corpusPath}`);
  const corpus = await loadCorpus(corpusPath, config.chunkChars, config.chunkOverlap);
  if (!corpus.chunks.length) {
    console.error(`Corpus is empty: ${corpusPath}`);
    process.exit(1);
  }
  console.error(`[rlm] ${corpus.chunks.length} chunks loaded`);

  const client = new Anthropic({ apiKey: process.env.ANTHROPIC_API_KEY });

  const t0 = Date.now();
  const result = await runRLM(client, config, corpus, question, stage, (e) => {
    if (verbose) console.error(e);
  });
  const ms = Date.now() - t0;

  if (json) {
    console.log(JSON.stringify({ ...result, timeMs: ms }));
    return;
  }

  console.log("\n=== ANSWER ===\n");
  console.log(result.answer);
  console.log("\n=== STATS ===");
  console.log(`time:           ${(ms / 1000).toFixed(1)}s`);
  console.log(`iterations:     ${result.iterations}`);
  console.log(`repl calls:     ${result.replCalls}`);
  console.log(`critic cycles:  ${result.criticCycles}`);
  console.log(`tokens in/out:  ${result.totalInputTokens} / ${result.totalOutputTokens}`);
}

main().catch((e) => { console.error("Fatal:", e); process.exit(1); });
