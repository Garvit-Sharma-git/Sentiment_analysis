// src/api.ts
import axios from 'axios';

const API_BASE_URL = 'http://localhost:8000'; // or your Docker internal address if needed

export interface SentimentResponse {
  label: 'positive' | 'negative';
  score: number;
}

export const predictSentiment = async (text: string): Promise<SentimentResponse> => {
  const response = await axios.post(`${API_BASE_URL}/predict`, { text });
  return response.data;
};
