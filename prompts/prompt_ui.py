from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, pipeline
import torch
import streamlit as st

# Load model and tokenizer manually to avoid meta tensor issues
model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-small", device_map="cpu", torch_dtype=torch.float32)
tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-small")

# Create pipeline with loaded model
llm = pipeline("text2text-generation", model=model, tokenizer=tokenizer)

st.header('Research Tool')

user_input = st.text_input("Enter your question")

if st.button("answer"):
    if user_input:
        result = llm(user_input)[0]['generated_text']
        st.write(result)
    else:
        st.write("Please enter a question to answer.")
