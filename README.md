
# 🧠 Sentiment Analysis - Full Stack Application

  

A full-stack sentiment analysis web application that allows users to input text and receive a predicted sentiment (Positive or Negative) using a fine-tuned DistilBERT model.

  

---

  

## 🌐 Live Demo

  

Loom Link- https://www.loom.com/share/ee8f9fa6e0e84c42904b1f4373561670?sid=35fdf5f2-20cc-4179-897e-c44b3999cdbb
  

## 🔧 Environment Setup

  

Create the following `.env` files for frontend:

  

### `.env.production`

VITE_API_BASE_URL=https://sentiment-analysis-x8zw.onrender.com

  
  
  

### `.env.development`

VITE_API_BASE_URL=http://localhost:8000

  
  
  

Update your `api.ts` to use:

```ts

const  API_BASE_URL  =  import.meta.env.VITE_API_BASE_URL;
```
Make sure CORS is enabled in FastAPI like so:

  
  
```
allow_origins=[

"http://localhost:5173",

"https://sentiment-analysis-ten-ruddy.vercel.app"

]

  ```

---

  

## ✨ Features

  

- 🔍 Real-time Sentiment Prediction (Positive/Negative)

- 🤖 Transformer-based model (DistilBERT from Hugging Face)

- 🎨 Clean UI  with a grey theme

- 📦 FastAPI backend with Docker support

- ⚛️ React frontend with TailwindCSS

- ✅ Model fine-tuned on custom dataset

- 🐳 Dockerized for easy deployment

  

---

  

## 🛠️ Tech Stack

  

| Layer | Technology |

|-----------|--------------------------------------|

| Frontend | React, TypeScript, TailwindCSS |

| Backend | Python, FastAPI, Transformers (HF) |

|  ML Model |  DistilBERT (Fine-tuned via 🤗) |

| Docker | Backend containerized |

  

---

  

## 🚀 Quick Start

  

### 🔧 Backend (FastAPI + PyTorch)

  

1. Navigate to the backend directory:

``` bash

cd backend
```
Create virtual environment:

  
  
``` bash
python3 -m venv venv

source venv/bin/activate
```
Install dependencies:

  
  
``` bash
pip install -r requirements.txt
```
Start the backend:

  
  

python3 main.py

### 🌐 Frontend (React + TailwindCSS)

Navigate to frontend folder:

  
  
``` bash
cd frontend
```
Install dependencies:

  
  
``` bash
npm install
```
Run frontend:

  
  
``` bash
npm run dev
```
Open browser at: http://localhost:5173/

  

#### 🧪 Testing API

You can test the backend independently using:

  
  
``` bash
curl -X POST "http://127.0.0.1:8000/predict" \

-H "Content-Type: application/json" \

-d '{"text": "I love this product"}'
```
Response:

  
  
``` bash
{"label": "positive", "score": 0.9999}
```
### 🧠 Model

The backend/model/ folder contains the fine-tuned DistilBERT model artifacts:

  

model.safetensors

  

config.json

  

tokenizer.json

  

tokenizer_config.json

  

vocab.txt

  

📁 Project Structure

  
  

sentiment-analysis/

├── backend/

│ ├── main.py

│ ├── config.py

│ ├── model/

│ └── requirements.txt

├── frontend/

│ ├── src/

│ ├── index.html

│ └── tailwind.config.js

├── data.jsonl

├── finetune.py

└── README.md

### 📦 Docker (Optional)

To run backend using Docker:


  
``` bash
cd backend

docker build -t sentiment-backend .

docker run -p 8000:8000 sentiment-backend
```
### ✅ Deployment (Optional)

If needed, frontend can be deployed to Vercel:

  

Connect your GitHub repo

  

Set:

  

Framework Preset: Vite

  

Build Command: 
``` bash
npm run build
```
  

Output Directory: dist

  

### 🙌 Acknowledgements

Transformers by Hugging Face

  

FastAPI

  

TailwindCSS

  

Docker

  

#### 📬 Contact

Garvit Sharma

📧 garvitsharma@example.com

🔗 GitHub

  

📝 License

This project is licensed under the MIT License.

  
  
  

---

  



  

