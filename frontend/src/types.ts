// src/types.ts
export type SentimentLabel = 'positive' | 'negative';

export interface PredictionResult {
  label: SentimentLabel;
  score: number;
}
