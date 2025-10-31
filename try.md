# 🎬 AVRA — AI Video & Web Research Assistant (Multimodal Agentic RAG)

AVRA is a **multimodal AI research assistant** built with **Generative AI**, **LangChain**, and **agentic tools**.
It allows users to **ask questions about YouTube videos or documents**, fetch **grounded web context**, and generate **detailed, factual answers** using **retrieval-augmented generation (RAG)**.

---

## 🚀 Features

### 🧩 Multimodal Input

* 🖥️ Summarize YouTube videos using transcripts
* 📄 Process documents: `.txt`, `.pdf`, `.docx`, `.csv`, `.md`
* 🌐 Support for local files and URLs

### 🤖 Agentic AI & Web Integration

* ⚡ Uses **React Agent** for web search via **BrightData MCP**
* 🔍 Fetches authoritative, up-to-date web context for queries
* 🟢 Optional **SerpAPI integration** for additional search results

### 🧠 Grounded RAG Q&A

* 📚 Combines video transcripts, documents, and web context
* 📝 Uses **Gemini LLM** for answers strictly based on retrieved content
* 🕵️ Generates **detailed, 200–300 word answers** with citations
* ⚖️ Ensures accuracy: never invents facts or assumptions

### 💾 Vector Store & Retrieval

* 🧠 **FAISS-based embeddings** for semantic search
* 🔧 MultiQueryRetriever with **contextual compression** for concise, relevant context
* 🔄 Efficient handling of large datasets (videos/documents)

### 📊 User Dashboard & Insights

* 🎛️ Streamlit-based UI with tabs:

  * **Ask Question** – Query videos/documents and get AI-generated answers
  * **Summaries** – TL;DR summaries of videos/documents
  * **User Analysis** – Query metrics, context usage, frequent words
* 💾 Optionally cache transcripts & embeddings for faster reuse

---

## 🏗️ Tech Stack

| Category                          | Technology                                                 |
| --------------------------------- | ---------------------------------------------------------- |
| **Backend & AI**                  | Python 3.13, Gemini LLM, HuggingFace Embeddings, LangChain |
| **Web Agents**                    | BrightData MCP, LangGraph React Agent, SerpAPI             |
| **Vector Store**                  | FAISS, MultiQueryRetriever, ContextualCompressionRetriever |
| **Frontend/UI**                   | Streamlit                                                  |
| **File Processing**               | Docling, UnstructuredMarkdownLoader, TextLoader            |
| **Data Analysis & Visualization** | Pandas, Plotly                                             |

---

## ⚙️ Installation & Setup

1. Clone the repository:
   `git clone https://github.com/<your-username>/AVRA.git`
   `cd AVRA`

2. Create and activate a virtual environment:
   `python -m venv venv`
   `source venv/Scripts/activate`  # Windows
   `source venv/bin/activate`      # macOS/Linux

3. Install dependencies:
   `pip install -r requirements.txt`

4. Setup environment variables in a `.env` file:

```
API_KEY=<your_gemini_api_key>
BRIGHT_DATA_API_TOKEN=<your_brightdata_token>
WEB_UNLOCKER_ZONE=unblocker
BROWSER_ZONE=scraping_browser
SERPAPI_API_KEY=<your_serpapi_key>
```

5. Run the app:
   `streamlit run app.py`
   Open your browser at `http://127.0.0.1:8501/`

---

## 📝 How It Works

1. Input a **YouTube URL** or upload documents.
2. AVRA fetches transcripts or loads content.
3. Creates a **vector store** for semantic search.
4. Uses **agentic AI tools** to fetch relevant web context.
5. Combines context and LLM to generate **grounded answers**.
6. Provides **summaries** and **user insights** in Streamlit UI.

---

## 🧠 Key Highlights

* 🔹 **Agentic AI workflow:** Combines LLMs with web search agents
* 🔹 **Multimodal support:** Videos + documents
* 🔹 **MCP integration:** BrightData-based automated web retrieval
* 🔹 **Grounded answers:** Fact-checked, citation-enabled, no hallucinations
* 🔹 **Analytics:** Query history, web usage, answer length, common words

---

## 📁 Project Structure

```
avra/
├── app.py                # Streamlit frontend
├── agent.py              # React agent setup
├── llm.py                # LLM and embeddings
├── vector.py             # Vector store creation
├── retriver.py           # RAG retriever setup
├── yt_transcript.py      # YouTube transcript fetching
├── utils.py              # Helper functions
├── prompt.py             # Prompt templates
├── config.py             # MCP client configuration
├── cache/                # Cached transcripts & embeddings
└── report/               # Uploaded files & temporary processing
```

---

## 🧠 Future Enhancements

* Add **multi-video cross-referencing**
* Support **PDF and video summarization with AI highlights**
* Advanced **analytics dashboard** for user insights
* Additional AI models: summarization, SEO, sentiment analysis

---

## 👨‍💻 Author

Developed by: [Ayush Ghosh](https://github.com/ai-codesmith-solver)
🎓 Python Developer | Django | GenAI | Agentic AI | MCP Integration

---

## ⭐ Support

If you like this project, please ⭐ it on GitHub! Contributions and suggestions are welcome.

---

## 🪄 License

MIT License — free to use and modify.
