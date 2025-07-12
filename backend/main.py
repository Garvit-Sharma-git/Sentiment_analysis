import os
import torch
import onnxruntime as ort
from fastapi import FastAPI
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
from fastapi.middleware.cors import CORSMiddleware

MODEL_PATH = "./model"
USE_FINETUNED = os.path.exists(MODEL_PATH) and os.listdir(MODEL_PATH)
USE_ONNX = os.getenv("USE_ONNX", "false").lower() == "true"

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173","https://your-frontend-url.vercel.app",],  # Frontend dev port or replace with prod
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TextInput(BaseModel):
    text: str

# Lazy load variables
tokenizer = None
model = None
pipe = None
session = None

@app.post("/predict")
def predict_sentiment(input: TextInput):
    global tokenizer, model, pipe, session

    if USE_ONNX:
        print("🚀 Using ONNX Runtime for inference")

        if tokenizer is None or session is None:
            tokenizer = AutoTokenizer.from_pretrained(
                MODEL_PATH if USE_FINETUNED else "distilbert-base-uncased-finetuned-sst-2-english"
            )
            session = ort.InferenceSession("model.onnx")

        inputs = tokenizer(input.text, return_tensors="np", truncation=True, padding=True)
        outputs = session.run(None, {
            "input_ids": inputs["input_ids"],
            "attention_mask": inputs["attention_mask"]
        })
        scores = outputs[0][0]
        label = "positive" if scores[1] > scores[0] else "negative"
        confidence = float(max(scores))
        return {"label": label, "score": round(confidence, 4)}

    else:
        print("⚙️ Using PyTorch pipeline")

        if pipe is None:
            tokenizer = AutoTokenizer.from_pretrained(
                MODEL_PATH if USE_FINETUNED else "distilbert-base-uncased-finetuned-sst-2-english"
            )
            model = AutoModelForSequenceClassification.from_pretrained(
                MODEL_PATH if USE_FINETUNED else "distilbert-base-uncased-finetuned-sst-2-english"
            )
            pipe = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer, device=-1)

        result = pipe(input.text)[0]
        return {"label": result["label"].lower(), "score": round(result["score"], 4)}
