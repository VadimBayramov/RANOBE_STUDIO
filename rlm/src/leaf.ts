import Anthropic from "@anthropic-ai/sdk";
import type { Chunk } from "./types.js";

export type LeafResult = {
  answer: string;
  inputTokens: number;
  outputTokens: number;
};

const LEAF_SYSTEM = `You are a leaf-agent in a Recursive Language Model (RLM) pipeline.
You receive ONE chunk of text and ONE focused sub-question.

Rules:
- Answer in 1-4 sentences. Concise, factual, no preamble.
- Quote short verbatim snippets (≤25 words) only when they directly answer the question.
- If the chunk does not contain the answer, reply exactly: NOT_FOUND
- Never speculate beyond the chunk. Never invent details.
- Do NOT echo the whole chunk back. Extract the relevant signal only.`;

export async function leafAgent(
  client: Anthropic,
  model: string,
  chunk: Chunk,
  subQuestion: string
): Promise<LeafResult> {
  const resp = await client.messages.create({
    model,
    max_tokens: 1024,
    system: LEAF_SYSTEM,
    messages: [
      {
        role: "user",
        content: `<chunk id="${chunk.id}" source="${chunk.source}">
${chunk.text}
</chunk>

Sub-question: ${subQuestion}`
      }
    ]
  });

  const textBlock = resp.content.find((b) => b.type === "text");
  const answer = textBlock && textBlock.type === "text" ? textBlock.text.trim() : "NOT_FOUND";

  return {
    answer,
    inputTokens: resp.usage.input_tokens,
    outputTokens: resp.usage.output_tokens
  };
}
