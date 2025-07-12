// src/components/SentimentResult.tsx
import React from 'react';
import type { PredictionResult } from '../types';

interface Props {
  result: PredictionResult | null;
}

const SentimentResult: React.FC<Props> = ({ result }) => {
  if (!result) return null;

  return (
    <div style={{ marginTop: 20, textAlign: 'center' }}>
      <h2>Prediction Result</h2>
      <p><strong>Label:</strong> {result.label}</p>
      <p><strong>Score:</strong> {result.score.toFixed(4)}</p>
    </div>
  );
};

export default SentimentResult;
