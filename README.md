# 🏆 AI-Powered Sports Quiz Generation Agent

An AI-powered Sports Quiz Generation application that creates engaging sports-related multiple-choice quizzes using **Retrieval-Augmented Generation (RAG)**. The system retrieves relevant sports knowledge from **ChromaDB** and leverages **Google Gemini** to generate factually grounded quiz questions. For recent sports information, it can also utilize web search to improve the relevance and freshness of the generated content.

---

# 🎥 Demo Video

A complete walkthrough of the project is available here:

**📹 Screen Recording:**  
[SPORTS_QUIZ_AGENT](https://drive.google.com/file/d/1wXznIdr9bW-LKF_BHp6UvqR_uz_Lvfv5/view?usp=drive_link)

The demo includes:
- Sport selection
- Difficulty selection
- Quiz generation
- Quiz regeneration
- ChromaDB knowledge retrieval
- Web search integration
- Generated quiz with explanations

---

# 📌 Project Overview

Traditional sports content on social media mainly consists of news, highlights, and opinion-based posts. This project introduces an interactive content format by automatically generating sports quizzes that encourage audience participation and increase engagement.

The application combines Retrieval-Augmented Generation (RAG) with a Large Language Model to generate unique, engaging, and factually accurate sports quizzes.

---

# ✨ Features

- Select a sport
- Select quiz difficulty (Easy / Medium / Hard)
- Generate multiple-choice sports quizzes
- Regenerate new quizzes
- Retrieve relevant sports knowledge using ChromaDB
- Use web search for recent sports information
- Generate:
  - Multiple-choice questions
  - Four answer options
  - Correct answer
  - Short explanation

---

# 🏗️ System Architecture

```
[User Input: "Football, Hard"]
       │
       ▼
 ┌───────────┐     1. Search local facts database  ──> [ChromaDB Vector Store]
 │ AI Agent  │ ──> 2. Search live internet news    ──> [DuckDuckGo Search]
 └───────────┘
       │
       ▼  (Retrieves text snippets)
 ┌────────────────────────────────────────────────────────┐
 │ Combined Context + Prompt Construction                 │
 └────────────────────────────────────────────────────────┘
       │
       ▼  (Sends highly specific request)
 ┌───────────────────┐
 │LLM (OpenAI/Gemini)│
 └───────────────────┘
       │
       ▼  (Generates structured response)
 [Four Multiple Choice Questions displayed in Streamlit UI]
```

---

# 🔄 Project Workflow

```
User Input
     │
     ▼
Select Sport & Difficulty
     │
     ▼
Retrieve Context from ChromaDB
     │
     ▼
Retrieve Latest Sports Information (DuckDuckGo)
     │
     ▼
Combine Retrieved Context
     │
     ▼
Generate Quiz using Gemini
     │
     ▼
Display Quiz in Streamlit
```


# 🛠️ Tech Stack

### Programming Language

- Python

### Frontend

- Streamlit

### AI / LLM

- Google Gemini

### Retrieval-Augmented Generation

- ChromaDB

### Embeddings

- Sentence Transformers

### Search

- DuckDuckGo Search

### Other Libraries

- LangChain
- python-dotenv

---

# 📂 Project Structure

```
sports-quiz-agent/
│
├── .env                  # Hidden file containing sensitive API keys
├── requirements.txt      # List of dependencies to install
├── README.md             # Guide on installation and execution
│
├── data/
│   └── sports_facts.json # Local historic database (raw facts in JSON format)
│
├── chroma_db/            # Created automatically by ChromaDB to store vector files
│
├── src/
│   ├── __init__.py       # Tells Python to treat src as an importable module
│   ├── config.py         # Handles importing API keys and system paths
│   ├── database.py       # Interacts only with ChromaDB (Insert & Query)
│   ├── search.py         # Interacts only with DuckDuckGo Search API
│   └── generator.py      # Combines context, builds prompt, and runs the LLM
│
└── app.py                # The front-end UI. Coordinates everything and renders it.

```

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/<YOUR_GITHUB_USERNAME>/sports-quiz-agent.git
cd sports-quiz-agent
```

---

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure Environment Variables

Create a `.env` file in the project root.

Example:

```env
GEMINI_API_KEY=your_google_gemini_api_key
```

Replace `your_google_gemini_api_key` with your own API key.

---

# ▶️ Running the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your browser at:

```
http://localhost:8501
```

---

# 🚀 How It Works

1. The user selects a **sport** and **difficulty level**.
2. The AI agent retrieves relevant sports facts from **ChromaDB** using semantic similarity search.
3. If recent or time-sensitive information is needed, the agent performs a **DuckDuckGo web search**.
4. The retrieved context from both sources is combined into a single prompt.
5. The prompt is sent to **Google Gemini**, which generates:
   - Four to five multiple-choice questions
   - Four answer options (A, B, C, D)
   - Correct answer
   - Short explanation
6. The generated quiz is displayed in the **Streamlit** dashboard.

---

# 🧠 RAG Workflow

```
Offline Sports Knowledge
           │
           ▼
       ChromaDB
           │
           ▼
 Similarity Search
           │
           ▼
 Relevant Context
           │
           ├──────────────┐
           │              │
           ▼              ▼
     Web Search     Recent Sports News
           │              │
           └──────┬───────┘
                  ▼
        Combined Context
                  │
                  ▼
        Google Gemini LLM
                  │
                  ▼
        Quiz Generation
```

---

# 🎯 Supported Difficulty Levels

- Easy
- Medium
- Hard

---

# 📋 Example Output

```
Sport: Cricket

Difficulty: Easy

Question:
Which two countries compete in The Ashes?

A. India and Pakistan

B. Australia and England

C. South Africa and New Zealand

D. Sri Lanka and West Indies

Correct Answer:
B. Australia and England

Explanation:
The Ashes is one of cricket's oldest and most famous Test cricket rivalries between Australia and England.
```

---

# ✅ Assignment Requirements Covered

- ✔ Sport selection
- ✔ Difficulty selection
- ✔ Multiple-choice quiz generation
- ✔ Quiz regeneration
- ✔ ChromaDB integration
- ✔ Retrieval-Augmented Generation (RAG)
- ✔ Web search integration
- ✔ Streamlit dashboard
- ✔ Grounded quiz generation using retrieved knowledge

---

# 🔮 Future Improvements

- Support additional sports
- User authentication
- Quiz history
- Export quizzes
- Social media-ready quiz cards
- Leaderboard and scoring system
- Multilingual quiz generation
- Performance optimization

---
