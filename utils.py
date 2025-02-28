
import torch
import openai

def load_model(model_path):
    model = torch.load(model_path)
    model.eval()
    return model

def generate_math_problem(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]
