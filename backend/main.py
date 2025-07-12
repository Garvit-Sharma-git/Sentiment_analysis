# # backend/main.py

# from fastapi import FastAPI, HTTPException, Request
# from pydantic import BaseModel
# from typing import List
# from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification, TFAutoModelForSequenceClassification
# import torch
# import os
# from fastapi.middleware.cors import CORSMiddleware

# # ===================== CONFIG =====================
# MODEL_FRAMEWORK = os.getenv("MODEL_FRAMEWORK", "pytorch")  # Set "tensorflow" to use TF

# MODEL_PATH = "./model"
# USE_FINETUNED = os.path.exists(MODEL_PATH) and os.listdir(MODEL_PATH)

# # ===================== MODEL LOADING =====================
# if USE_FINETUNED:
#     print("🔁 Loading fine-tuned model from ./model")
#     tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
#     if MODEL_FRAMEWORK == "tensorflow":
#         model = TFAutoModelForSequenceClassification.from_pretrained(MODEL_PATH)
#     else:
#         model = AutoModelForSequenceClassification.from_pretrained(MODEL_PATH)
# else:
#     print("⬇️  Loading default pretrained model from Hugging Face")
#     tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")
#     if MODEL_FRAMEWORK == "tensorflow":
#         model = TFAutoModelForSequenceClassification.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")
#     else:
#         model = AutoModelForSequenceClassification.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")

# framework = "tf" if MODEL_FRAMEWORK == "tensorflow" else "pt"
# device = torch.device("cpu")  # Always use CPU for now
# pipe = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer, device=-1, framework=framework)

# # ===================== APP SETUP =====================
# app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["http://localhost:5173"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # ===================== ROUTES =====================
# class TextInput(BaseModel):
#     text: str

# class BatchInput(BaseModel):
#     texts: List[str]

# @app.post("/predict")
# def predict_sentiment(input: TextInput):
#     try:
#         result = pipe(input.text)[0]
#         return {
#             "label": result["label"].lower(),
#             "score": round(result["score"], 4)
#         }
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

# @app.post("/predict-batch")
# def predict_batch(input: BatchInput):
#     try:
#         results = pipe(input.texts)
#         return [
#             {
#                 "label": r["label"].lower(),
#                 "score": round(r["score"], 4)
#             }
#             for r in results
#         ]
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

# backend/main.py

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
    allow_origins=["http://localhost:5173"],  # Frontend dev port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TextInput(BaseModel):
    text: str

if USE_ONNX:
    print("🚀 Using ONNX Runtime for inference")
    tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH if USE_FINETUNED else "distilbert-base-uncased-finetuned-sst-2-english")
    session = ort.InferenceSession("model.onnx")

    def predict(text: str):
        inputs = tokenizer(text, return_tensors="np", truncation=True, padding=True)
        outputs = session.run(None, {"input_ids": inputs["input_ids"], "attention_mask": inputs["attention_mask"]})
        scores = outputs[0][0]
        label = "positive" if scores[1] > scores[0] else "negative"
        confidence = float(max(scores))
        return {"label": label, "score": round(confidence, 4)}
else:
    print("⚙️ Using PyTorch pipeline")
    tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH if USE_FINETUNED else "distilbert-base-uncased-finetuned-sst-2-english")
    model = AutoModelForSequenceClassification.from_pretrained(MODEL_PATH if USE_FINETUNED else "distilbert-base-uncased-finetuned-sst-2-english")
    pipe = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer, device=-1)

    def predict(text: str):
        result = pipe(text)[0]
        return {"label": result["label"].lower(), "score": round(result["score"], 4)}

@app.post("/predict")
def predict_sentiment(input: TextInput):
    return predict(input.text)
