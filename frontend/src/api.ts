// src/api.ts
import axios from 'axios';

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL;

export interface SentimentResponse {
  label: 'positive' | 'negative';
  score: number;
}

export const predictSentiment = async (text: string): Promise<SentimentResponse> => {
  const response = await axios.post(`${API_BASE_URL}/predict`, { text });
  return response.data;
};
