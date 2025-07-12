# finetune.py

import argparse
import json
import os
import random
from pathlib import Path

import numpy as np
import torch
from datasets import load_dataset, Dataset
from transformers import (
    AutoTokenizer,
    AutoModelForSequenceClassification,
    Trainer,
    TrainingArguments,
    set_seed,
)

MODEL_NAME = "distilbert-base-uncased"
LABEL2ID = {"negative": 0, "positive": 1}
ID2LABEL = {0: "negative", 1: "positive"}
OUTPUT_DIR = "./model"

def parse_args():
    parser = argparse.ArgumentParser(description="Fine-tune a sentiment model.")
    parser.add_argument("--data", required=True, help="Path to JSONL dataset.")
    parser.add_argument("--epochs", type=int, default=3, help="Number of training epochs.")
    parser.add_argument("--lr", type=float, default=3e-5, help="Learning rate.")
    return parser.parse_args()

def set_all_seeds(seed=42):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    set_seed(seed)

def load_data(jsonl_path):
    with open(jsonl_path, "r") as f:
        samples = [json.loads(line) for line in f]
    texts = [s["text"] for s in samples]
    labels = [LABEL2ID[s["label"]] for s in samples]
    return Dataset.from_dict({"text": texts, "label": labels})

def tokenize(batch, tokenizer):
    return tokenizer(batch["text"], truncation=True, padding="max_length", max_length=128)

def main():
    args = parse_args()
    set_all_seeds()

    dataset = load_data(args.data)
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    dataset = dataset.map(lambda x: tokenize(x, tokenizer), batched=True)
    dataset.set_format(type="torch", columns=["input_ids", "attention_mask", "label"])

    model = AutoModelForSequenceClassification.from_pretrained(
        MODEL_NAME,
        num_labels=2,
        id2label=ID2LABEL,
        label2id=LABEL2ID,
    )

    training_args = TrainingArguments(
        output_dir="./results",
        evaluation_strategy="no",
        per_device_train_batch_size=16,
        num_train_epochs=args.epochs,
        learning_rate=args.lr,
        weight_decay=0.01,
        logging_steps=10,
        save_strategy="no",
        disable_tqdm=False,
        seed=42,
        report_to="none",
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=dataset,
    )

    trainer.train()

    Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)
    model.save_pretrained(OUTPUT_DIR)
    tokenizer.save_pretrained(OUTPUT_DIR)

    print(f"✅ Model fine-tuned and saved to {OUTPUT_DIR}")

if __name__ == "__main__":
    main()
