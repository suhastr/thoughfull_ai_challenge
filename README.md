# 🧠 Thoughtful AI Support Bot

A smart AI-powered support bot that answers user queries using a combination of semantic search (TF-IDF + cosine similarity) and LLaMA-4 fallback via Groq API.

> Built with Streamlit + Groq + Python — hosted on Replit.

---

## 🚀 Features

- ✅ Answers common questions from a `faq.json` knowledge base.
- 💡 Uses **TF-IDF + cosine similarity** for semantic search.
- 🤖 If no match is found, falls back to **Groq’s LLaMA-4** model.
- 🎯 Clean UI built with Streamlit.
- 🔒 API key securely loaded from `.env` (or `.api_key` if preferred).

---

## 📁 Project Structure

```
.
├── main.py           # Main app logic
├── faq.json          # List of FAQs with answers
├── requirements.txt  # Dependencies
├── README.md         # This file
├── .env              # (Hidden) API key file
└── .replit           # Replit config
```

---

## ⚙️ Running Locally

> You can also run this project on [Replit](https://replit.com) (preferred by Thoughtful AI challenge reviewers).

### 1. Clone the repo
```bash
git clone https://github.com/YOUR_USERNAME/thoughtful-ai-support-bot.git
cd thoughtful-ai-support-bot
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Add API key
Create a `.env` file with:
```
GROQ_API_KEY=your_api_key_here
```

### 4. Start the Streamlit app
```bash
streamlit run main.py
```

---

## 🧪 Test Scenarios & Example Questions

Test your bot's behavior across all key cases:

---

### 🔹 Case 1: ✅ Exact Match from `faq.json`
These questions are **predefined** and will return direct answers:

- `What does EVA do?`
- `What does the eligibility verification agent (EVA) do?`
- `Can you tell me what EVA is used for?`

---

### 🔹 Case 2: 🧠 Semantic Match (Near Match)
These aren’t exact, but semantically similar to entries in `faq.json`:

- `How does Thoughtful AI compare with OpenAI?`
- `Compare Thoughtful AI and OpenAI.`
- `Is Thoughtful better than OpenAI?`

---

### 🔹 Case 3: 🤖 No Match — Uses Fallback (Groq API)
Bot will call the LLaMA-4 model to generate a smart response:

- `What is the capital of France?`
- `Tell me how to deploy a Django app.`
- `Explain Kubernetes briefly.`

---

### 🔹 Case 4: ❌ Low Relevance or Garbage Input
Test fallback or error handling when no useful match is found:

- `asdflkjqweroij`
- `!!!!!!!?????`
- (Just press enter with empty input)

---

## 📦 Hosted Version (Replit)
👉 View the app here:  
[https://thoughtful-ai-support-bot.trushas21.repl.co](https://thoughtful-ai-support-bot.trushas21.repl.co)

---

## 👨‍💻 Author

**Suhas Thandaga Ramesh**  
Built with ❤️ using Streamlit + Groq + Python.

---

## 📝 License

MIT License — free to use and modify.
