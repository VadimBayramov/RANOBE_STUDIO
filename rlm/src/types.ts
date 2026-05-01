export type Chunk = {
  id: string;
  source: string;
  index: number;
  text: string;
};

export type Corpus = {
  chunks: Chunk[];
  byId: Map<string, Chunk>;
};

export type RLMConfig = {
  orchestratorModel: string;
  leafModel: string;
  criticModel: string;
  maxIterations: number;
  criticIterations: number;
  chunkChars: number;
  chunkOverlap: number;
};

export type RunResult = {
  answer: string;
  iterations: number;
  criticCycles: number;
  replCalls: number;
  totalInputTokens: number;
  totalOutputTokens: number;
};
