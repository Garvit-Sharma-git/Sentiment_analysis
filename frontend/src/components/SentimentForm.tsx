// src/components/SentimentForm.tsx
import React, { useState } from 'react';
import { predictSentiment } from '../api';
import type { PredictionResult } from '../types';

interface Props {
  onResult: (result: PredictionResult) => void;
}

const SentimentForm: React.FC<Props> = ({ onResult }) => {
  const [text, setText] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setError(null);

    try {
      const result = await predictSentiment(text);
      onResult(result);
    } catch (err) {
      setError('Failed to predict sentiment.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <form onSubmit={handleSubmit} style={{ maxWidth: 600, margin: 'auto' }}>
      <textarea
        value={text}
        onChange={(e) => setText(e.target.value)}
        rows={5}
        placeholder="Enter text to analyze..."
        style={{ width: '100%', padding: 12 }}
      />
      <button type="submit" disabled={loading || !text.trim()} style={{ marginTop: 10 }}>
        {loading ? 'Analyzing...' : 'Predict'}
      </button>
      {error && <p style={{ color: 'red' }}>{error}</p>}
    </form>
  );
};

export default SentimentForm;
