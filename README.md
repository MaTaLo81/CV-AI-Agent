# 🤖 CV AI Agent

An AI-powered assistant that allows recruiters and collaborators to explore the professional experience through natural language.

👉 Ask questions like:

* “Does Marcos have experience in finance?”
* “What tools does he use?”
* “Is he a good fit for a data role?”

---

## 🚀 Live demo:

👉 https://marcos-cv-agent.streamlit.app

## The public repo:
  
👉 https://github.com/MaTaLo81/CV-AI-Agent

---

## 🧠 What it does

This project uses Retrieval-Augmented Generation (RAG) to provide accurate, context-aware answers based on my CV and professional background.

---

## 🏗️ Architecture

```text
User Question
     ↓
Retriever (FAISS)
     ↓
Relevant CV Chunks
     ↓
LLM (OpenAI)
     ↓
Generated Answer
```

---

## ⚙️ Tech Stack

* Python
* Streamlit
* LangChain
* OpenAI API
* FAISS (vector database)
* PDF/Text processing

---

## 📦 Features

* 🔍 Semantic search over CV content
* 🧠 Context-aware answers using LLMs
* 📄 TXT CV ingestion pipeline
* ⚡ Fast retrieval with FAISS
* 🌐 Interactive web interface

---

## 🛠️ How it works

1. CV is loaded and chunked
2. Text is converted into embeddings
3. Stored in a FAISS vector database
4. User queries retrieve relevant chunks
5. LLM generates a grounded answer

---

## 🧪 Example Questions

* “What industries has Marcos worked in?”
* “Does he have experience with machine learning?”
* “What was his last role?”

---

## 👤 About Me

I’m Marcos Taboada. I lead SaaS and AI transformation programs and build scalable, real-world solutions.

🔗 LinkedIn: https://www.linkedin.com/in/marcostaboadalorenzo/
💻 GitHub: https://github.com/MaTaLo81

---

## ⚠️ Disclaimer

This AI assistant represents my professional experience and aims to provide accurate answers.
Feel free to ask follow-up questions to clarify any details.

---

## 🚀 Future Improvements

* Job matching / fit scoring
* Improved chunking strategies
* Enhanced UI/UX
* Multi-document support (projects, LinkedIn, etc.)

---

## 📌 Versions

v1.0 – Initial release

---

## 🛠️ Setup & Run Instructions

Follow these steps to run the project locally:
⚠️ Note: This project requires an OpenAI API key.

---

### 1. Clone the repository

```bash
git clone https://github.com/MaTaLo81/marcos-cv-agent.git
cd marcos-cv-agent
```

---

### 2. Create required folder structure

```bash
mkdir -p data/embeddings
mkdir -p data/processed
mkdir -p data/raw
```

---

### 3. Create environment variables

Create a `.env` file in the root directory:

```text
OPENAI_API_KEY=sk-...
```

---

### 4. Create and activate a virtual environment (recommended)

```bash
python -m venv venv
```

Activate it:

* **Windows (Git Bash):**

```bash
source venv/Scripts/activate
```

* **Windows (CMD):**

```bash
venv\Scripts\activate
```

* **Mac/Linux:**

```bash
source venv/bin/activate
```

---

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 6. Add your CV

Place your CV (in `.txt` format) inside:

```text
data/raw/
```

Then update the path in:

```python
# ingestion/embed.py
DATA_PATH = "data/raw/your_cv.txt"
```

---

### 7. Generate embeddings

```bash
python -m ingestion.embed
```

---

### 8. Configure your profile

Update your personal information in:

```text
utils/config.py
```

---

### 9. Run the app

```bash
streamlit run app/main.py
```

---

### 🎉 Done!

Open your browser and start interacting with your AI assistant.

Have fun exploring your AI-powered CV 🚀
