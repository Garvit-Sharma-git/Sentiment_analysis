# 🧠 Sentiment Analysis - Full Stack Application

A full-stack sentiment analysis web application that allows users to input text and receive a predicted sentiment (Positive or Negative) using a fine-tuned DistilBERT model.

---

## ✨ Features

- 🔍 Real-time Sentiment Prediction (Positive/Negative)
- 🤖 Transformer-based model (DistilBERT from Hugging Face)
- 🎨 Clean UI with a grey theme
- 📦 FastAPI backend with Docker support
- ⚛️ React frontend with TailwindCSS
- ✅ Model fine-tuned on custom dataset
- 🐳 Dockerized for easy deployment

---

## 🛠️ Tech Stack

| Layer     | Technology                           |
|-----------|--------------------------------------|
| Frontend  | React, TypeScript, TailwindCSS       |
| Backend   | Python, FastAPI, Transformers (HF)   |
| ML Model  | DistilBERT (Fine-tuned via 🤗)        |
| Docker    | Backend containerized                |

---

## 🚀 Quick Start

### 🔧 Backend (FastAPI + PyTorch)

1. Navigate to the backend directory:
   ```bash
   cd backend
Create virtual environment:

bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Start the backend:

bash
Copy
Edit
python3 main.py
🌐 Frontend (React + TailwindCSS)
Navigate to frontend folder:

bash
Copy
Edit
cd frontend
Install dependencies:

bash
Copy
Edit
npm install
Run frontend:

bash
Copy
Edit
npm run dev
Open browser at: http://localhost:5173/

🧪 Testing API
You can test the backend independently using:

bash
Copy
Edit
curl -X POST "http://127.0.0.1:8000/predict" \
     -H "Content-Type: application/json" \
     -d '{"text": "I love this product"}'
Response:

json
Copy
Edit
{"label": "positive", "score": 0.9999}
🧠 Model
The backend/model/ folder contains the fine-tuned DistilBERT model artifacts:

model.safetensors

config.json

tokenizer.json

tokenizer_config.json

vocab.txt

📁 Project Structure
arduino
Copy
Edit
sentiment-analysis/
├── backend/
│   ├── main.py
│   ├── config.py
│   ├── model/
│   └── requirements.txt
├── frontend/
│   ├── src/
│   ├── index.html
│   └── tailwind.config.js
├── data.jsonl
├── finetune.py
└── README.md
📦 Docker (Optional)
To run backend using Docker:

bash
Copy
Edit
cd backend
docker build -t sentiment-backend .
docker run -p 8000:8000 sentiment-backend
✅ Deployment (Optional)
If needed, frontend can be deployed to Vercel:

Connect your GitHub repo

Set:

Framework Preset: Vite

Build Command: npm run build

Output Directory: dist

🙌 Acknowledgements
Transformers by Hugging Face

FastAPI

TailwindCSS

Docker

📬 Contact
Garvit Sharma
📧 garvitsharma@example.com
🔗 GitHub

📝 License
This project is licensed under the MIT License.

yaml
Copy
Edit

---

### ✅ Next Steps

- Copy the content above and save it in a file called `README.md` at the **root** of your project.
- Run:
  ```bash
  git add README.md
  git commit -m "Add project README"
  git push