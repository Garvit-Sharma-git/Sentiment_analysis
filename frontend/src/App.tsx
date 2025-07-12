// src/App.tsx
import React, { useState } from 'react';
import SentimentForm from './components/SentimentForm';
import SentimentResult from './components/SentimentResult';
import type { PredictionResult } from './types';

function App() {
  const [result, setResult] = useState<PredictionResult | null>(null);

  return (
    <div style={{ padding: '2rem', fontFamily: 'Arial, sans-serif' }}>
      <h1 style={{ textAlign: 'center' }}>Sentiment Analyzer</h1>
      <SentimentForm onResult={setResult} />
      <SentimentResult result={result} />
    </div>
  );
}

export default App;
