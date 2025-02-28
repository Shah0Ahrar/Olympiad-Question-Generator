
import torch
import pandas as pd
from transformers import GPT2LMHeadModel, GPT2Tokenizer

df = pd.read_csv("data/cleaned_olympiad_questions.csv")
model = GPT2LMHeadModel.from_pretrained("gpt2")
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

def train():
    inputs = tokenizer(df["question"].tolist(), return_tensors="pt", padding=True, truncation=True)
    outputs = model(**inputs, labels=inputs["input_ids"])
    loss = outputs.loss
    loss.backward()
    torch.save(model, "model/olympiad_model.pth")
    print("✅ Model trained and saved!")

train()
