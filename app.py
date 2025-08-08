import streamlit as st
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from datetime import datetime
import json
import os

# Title and description
st.set_page_config(page_title="Desi Drama GPT", layout="centered")
st.title("🎭 Desi Drama GPT – Regional Skits Generator")
st.markdown("Create funny, desi-style skits between two characters in your native language!")

# Inputs
char1 = st.text_input("👤 Character 1", value="Dadi (Grandma)")
char2 = st.text_input("👤 Character 2", value="Postman")
topic = st.text_input("💬 Topic", value="WhatsApp and smartphones")
language = st.selectbox("🌐 Language", ["Hindi", "Tamil", "Telugu", "Punjabi", "Marathi", "Kannada", "Gujarati", "Bengali"])

# Load model and tokenizer
@st.cache_resource
def load_model():
    model_name = "microsoft/phi-2"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.float32)
    return tokenizer, model

tokenizer, model = load_model()

# Skit Generator
def generate_skit(character1, character2, topic, language):
    prompt = (
        f"Write a short, funny skit in {language} between two characters: {character1} and {character2}.\n"
        f"Topic: {topic}\n"
        f"Use regional slang, humor, and keep it 6-10 lines. Format like a play.\n\n"
        f"{character1}:"
    )
    inputs = tokenizer(prompt, return_tensors="pt")
    input_len = inputs["input_ids"].shape[1]
    outputs = model.generate(
        **inputs,
        max_new_tokens=150,
        temperature=0.8,
        do_sample=True,
        pad_token_id=tokenizer.eos_token_id,
    )
    result = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return result[input_len:].strip()

# Button
if st.button("🎬 Generate Skit"):
    if char1 and char2 and topic:
        with st.spinner("Generating your desi drama..."):
            skit = generate_skit(char1, char2, topic, language)
            st.markdown("### 🎭 Generated Skit:")
            st.code(f"{char1}: {skit}", language="text")

            # Save to corpus
            os.makedirs("corpus", exist_ok=True)
            data = {
                "timestamp": str(datetime.utcnow()),
                "character_1": char1,
                "character_2": char2,
                "topic": topic,
                "language": language,
                "skit": skit,
            }
            with open("corpus/desi_skit.jsonl", "a", encoding="utf-8") as f:
                f.write(json.dumps(data, ensure_ascii=False) + "\n")
    else:
        st.warning("Please fill in all fields.")

# Download button
if os.path.exists("corpus/desi_skit.jsonl"):
    with open("corpus/desi_skit.jsonl", "r", encoding="utf-8") as f:
        corpus_data = f.read()
    st.sidebar.download_button("⬇️ Download Corpus", corpus_data, file_name="desi_skit.jsonl")
