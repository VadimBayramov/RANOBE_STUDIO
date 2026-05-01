import { readdir, readFile, stat } from "node:fs/promises";
import { join, relative } from "node:path";
import type { Chunk, Corpus } from "./types.js";

const TEXT_EXTENSIONS = new Set([
  ".txt", ".md", ".markdown", ".json", ".jsonl", ".csv", ".tsv",
  ".ts", ".tsx", ".js", ".jsx", ".mjs", ".cjs",
  ".py", ".rb", ".go", ".rs", ".java", ".kt", ".swift",
  ".html", ".htm", ".css", ".scss", ".vue", ".svelte",
  ".yaml", ".yml", ".toml", ".ini", ".env", ".sh", ".fish", ".bash",
  ".log", ".sql", ".graphql", ".proto"
]);

async function walk(root: string): Promise<string[]> {
  const out: string[] = [];
  async function rec(dir: string) {
    const entries = await readdir(dir, { withFileTypes: true });
    for (const e of entries) {
      if (e.name.startsWith(".") || e.name === "node_modules" || e.name === "dist") continue;
      const full = join(dir, e.name);
      if (e.isDirectory()) await rec(full);
      else if (e.isFile()) out.push(full);
    }
  }
  const s = await stat(root);
  if (s.isFile()) return [root];
  await rec(root);
  return out;
}

function isTextFile(path: string): boolean {
  const dot = path.lastIndexOf(".");
  if (dot < 0) return true;
  return TEXT_EXTENSIONS.has(path.slice(dot).toLowerCase());
}

function chunkText(
  source: string,
  text: string,
  chunkChars: number,
  overlap: number
): Chunk[] {
  if (text.length <= chunkChars) {
    return [{ id: source, source, index: 0, text }];
  }
  const chunks: Chunk[] = [];
  let i = 0;
  let idx = 0;
  while (i < text.length) {
    const end = Math.min(i + chunkChars, text.length);
    chunks.push({
      id: `${source}#${idx}`,
      source,
      index: idx,
      text: text.slice(i, end)
    });
    if (end >= text.length) break;
    i = end - overlap;
    idx++;
  }
  return chunks;
}

export async function loadCorpus(
  rootPath: string,
  chunkChars: number,
  overlap: number
): Promise<Corpus> {
  const files = (await walk(rootPath)).filter(isTextFile);
  const chunks: Chunk[] = [];
  for (const f of files) {
    try {
      const text = await readFile(f, "utf8");
      if (!text.trim()) continue;
      const rel = relative(process.cwd(), f);
      chunks.push(...chunkText(rel, text, chunkChars, overlap));
    } catch {
      // skip unreadable
    }
  }
  const byId = new Map(chunks.map((c) => [c.id, c]));
  return { chunks, byId };
}

export function corpusSummary(corpus: Corpus): string {
  const bySource = new Map<string, number>();
  for (const c of corpus.chunks) {
    bySource.set(c.source, (bySource.get(c.source) ?? 0) + 1);
  }
  const lines: string[] = [];
  lines.push(`Corpus: ${corpus.chunks.length} chunks across ${bySource.size} sources.`);
  lines.push(`Sources (chunks per source):`);
  for (const [src, n] of bySource) {
    lines.push(`  - ${src} [${n}]`);
  }
  return lines.join("\n");
}
