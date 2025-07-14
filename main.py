import streamlit as st
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os
import re
from dotenv import load_dotenv
from groq import Groq

# Load keys from .api_key
load_dotenv(dotenv_path=".api_key")

# Initialize Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Clean text for better matching
def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", "", text)
    return text.strip()

# Load FAQ data
with open("faq.json", "r") as f:
    faq_data = json.load(f)["questions"]

questions = [item["question"] for item in faq_data]
answers = [item["answer"] for item in faq_data]
questions_cleaned = [clean_text(q) for q in questions]

# Vectorize questions
vectorizer = TfidfVectorizer().fit(questions_cleaned)
question_vectors = vectorizer.transform(questions_cleaned)

# Fallback with LLaMA-4
def call_llama_fallback(prompt):
    try:
        response = client.chat.completions.create(
            model="meta-llama/llama-4-scout-17b-16e-instruct",
            messages=[
                {"role": "system", "content": "You are a helpful assistant who answers questions clearly and concisely."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.5,
            max_completion_tokens=300,
            top_p=1,
            stream=False  # Important fix
        )
        return response.choices[0].message.content
    except Exception as e:
        return "Sorry, I couldn’t generate a fallback answer right now."

# Response logic
def get_best_answer(user_query):
    user_query_cleaned = clean_text(user_query)
    query_vector = vectorizer.transform([user_query_cleaned])
    similarities = cosine_similarity(query_vector, question_vectors).flatten()
    best_match_index = similarities.argmax()
    score = similarities[best_match_index]

    if score < 0.45:
        return call_llama_fallback(user_query)

    return answers[best_match_index]

# Streamlit UI
st.title("🧠 Thoughtful AI Support Bot")
st.write("Ask me anything about Thoughtful AI Agents.")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("Your question")

if user_input:
    reply = get_best_answer(user_input)
    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("Bot", reply))

for speaker, message in reversed(st.session_state.chat_history):
    st.markdown(f"**{speaker}:** {message}")
