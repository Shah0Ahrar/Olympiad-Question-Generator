
import streamlit as st
import torch
import pandas as pd
import random
import openai
from utils import load_model, generate_math_problem
from google_sheets import save_rating
from dotenv import load_dotenv
import os

# Load API keys from .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Load model and dataset
model = load_model("model/olympiad_model.pth")
df = pd.read_csv("data/cleaned_olympiad_questions.csv")

st.set_page_config(page_title="Olympiad Question Generator", layout="wide")
st.title("🧮 Olympiad Math Question Generator")

if st.button("Generate New Math Problem"):
    prompt = random.choice(df["question"])
    gpt_response = generate_math_problem(prompt)
    st.subheader("📝 Generated Math Problem:")
    st.write(gpt_response)

rating = st.slider("Rate the question (1-5):", 1, 5, 3)
if st.button("Submit Rating"):
    save_rating(gpt_response, rating)
    st.success("Thanks for your feedback!")
