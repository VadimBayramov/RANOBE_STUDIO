import { spawn } from "node:child_process";
import { createInterface } from "node:readline";
import type { ChildProcess } from "node:child_process";
import type { Writable, Readable } from "node:stream";
import Anthropic from "@anthropic-ai/sdk";
import type { Corpus } from "./types.js";
import { leafAgent } from "./leaf.js";

export type ExecResult = {
  stdout: string;
  error: string | null;
  final: string | null;
  leafInputTokens: number;
  leafOutputTokens: number;
};

export class ReplClient {
  private proc: ChildProcess & { stdin: Writable; stdout: Readable };
  private pending: Array<(line: string) => void> = [];
  private client: Anthropic;
  private leafModel: string;
  private corpus: Corpus;

  private constructor(
    proc: ChildProcess & { stdin: Writable; stdout: Readable },
    client: Anthropic,
    leafModel: string,
    corpus: Corpus
  ) {
    this.proc = proc;
    this.client = client;
    this.leafModel = leafModel;
    this.corpus = corpus;

    createInterface({ input: proc.stdout }).on("line", (line) => {
      const resolve = this.pending.shift();
      if (resolve) resolve(line);
    });
  }

  private readLine(): Promise<string> {
    return new Promise((resolve) => this.pending.push(resolve));
  }

  private send(obj: unknown) {
    this.proc.stdin.write(JSON.stringify(obj) + "\n");
  }

  static async create(client: Anthropic, leafModel: string, corpus: Corpus): Promise<ReplClient> {
    const proc = spawn("python3", ["repl_server.py"], { stdio: ["pipe", "pipe", "inherit"] }) as
      ChildProcess & { stdin: Writable; stdout: Readable };

    proc.on("error", (e) => {
      throw new Error(`REPL server failed to start: ${e.message}`);
    });

    const repl = new ReplClient(proc, client, leafModel, corpus);

    repl.send({
      chunks: corpus.chunks.map((c) => ({ id: c.id, source: c.source, text: c.text })),
    });

    const readyRaw = await repl.readLine();
    const ready = JSON.parse(readyRaw);
    if (ready.type !== "ready") throw new Error("REPL server init failed");

    return repl;
  }

  async exec(code: string): Promise<ExecResult> {
    let leafInputTokens = 0;
    let leafOutputTokens = 0;

    this.send({ type: "exec", code });

    // Read messages until "result" — handling cooperative sub_rlm() calls in between
    while (true) {
      const raw = await this.readLine();
      const msg = JSON.parse(raw);

      if (msg.type === "result") {
        return {
          stdout: msg.stdout ?? "",
          error: msg.error ?? null,
          final: msg.final ?? null,
          leafInputTokens,
          leafOutputTokens,
        };
      }

      if (msg.type === "sub_rlm") {
        const chunk = this.corpus.byId.get(msg.chunk_id);
        let result = "NOT_FOUND";
        if (chunk) {
          const r = await leafAgent(this.client, this.leafModel, chunk, msg.question);
          leafInputTokens += r.inputTokens;
          leafOutputTokens += r.outputTokens;
          result = r.answer;
        }
        this.send({ type: "sub_rlm_result", result });
      }
    }
  }

  destroy() {
    this.proc.stdin.end();
    this.proc.kill();
  }
}
