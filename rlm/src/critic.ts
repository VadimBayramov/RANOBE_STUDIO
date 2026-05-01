import Anthropic from "@anthropic-ai/sdk";

export type CriticVerdict = "APPROVED" | "REFINE";

export type CriticResult = {
  verdict: CriticVerdict;
  feedback: string;
  inputTokens: number;
  outputTokens: number;
};

const CRITIC_SYSTEM = `You are a critic reviewing an answer produced by a research agent.

Your job: check whether the answer fully addresses the user's question.

Rules:
- Be specific and brief. 2-5 sentences max.
- If the answer is complete and well-supported: respond with exactly "APPROVED"
- If there are gaps, missing evidence, or unanswered parts: start with "REFINE:" followed by a numbered list of specific issues.
  Example: "REFINE:\n1. Missing: how webhook signature is verified.\n2. Auth token expiry not addressed."
- Do NOT rewrite the answer. Only identify what is missing or wrong.
- Do NOT invent gaps. Only flag genuine omissions relative to the question.`;

export async function criticAgent(
  client: Anthropic,
  model: string,
  question: string,
  answer: string
): Promise<CriticResult> {
  const resp = await client.messages.create({
    model,
    max_tokens: 512,
    system: CRITIC_SYSTEM,
    messages: [
      {
        role: "user",
        content: `Question: ${question}\n\nAnswer to review:\n${answer}`
      }
    ]
  });

  const textBlock = resp.content.find((b) => b.type === "text");
  const text = textBlock && textBlock.type === "text" ? textBlock.text.trim() : "APPROVED";

  const verdict: CriticVerdict = text.startsWith("REFINE") ? "REFINE" : "APPROVED";

  return {
    verdict,
    feedback: text,
    inputTokens: resp.usage.input_tokens,
    outputTokens: resp.usage.output_tokens
  };
}
