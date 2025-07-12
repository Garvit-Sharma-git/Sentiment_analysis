# backend/export_to_onnx.py

from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch

MODEL_NAME = "distilbert-base-uncased-finetuned-sst-2-english"
model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

dummy_input = tokenizer("I love this product!", return_tensors="pt")
torch.onnx.export(
    model,
    (dummy_input["input_ids"], dummy_input["attention_mask"]),
    "model.onnx",
    input_names=["input_ids", "attention_mask"],
    output_names=["logits"],
    dynamic_axes={"input_ids": {0: "batch_size"}, "attention_mask": {0: "batch_size"}},
    opset_version=11
)

print("✅ Exported model to model.onnx")
