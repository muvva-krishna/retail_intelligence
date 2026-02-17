# 📊 Retail Intelligence RAG Pipeline using LlamaIndex + Gemini

## 🚀 Project Overview

This project demonstrates a production-style **Retrieval-Augmented Generation (RAG)** pipeline built on structured retail transaction data.

The goal is to:

- Preprocess structured business data
- Convert tabular rows into semantic documents
- Build a vector index
- Enable natural language querying over business data
- Combine numerical reasoning + semantic retrieval
- Orchestrate a full LLM-powered analytics pipeline

This project showcases:

- Data Engineering
- LLM Orchestration
- RAG Architecture
- Vector Indexing
- Query Routing
- Hybrid Analytics (Structured + Semantic)

This is designed as a strong portfolio project for Data Analyst / AI / GenAI roles.

---

# 🏗 Architecture Overview

```
Dataset (Excel)
        ↓
Preprocessing & Feature Engineering
        ↓
Structured DataFrame
        ↓
Document Creation (Row → Text)
        ↓
Embedding Generation (Gemini)
        ↓
Vector Index (SimpleVectorStore)
        ↓
Query Routing
   ├── PandasQueryEngine (Numeric questions)
   └── RAG Retriever (Semantic questions)
        ↓
LLM (Gemini Flash)
        ↓
Final Answer
```

---

# 📂 Project Structure

```
llamaindex-retail-rag/
│
├── data/
│   └── online_retail.xlsx
│
├── src/
│   ├── main.py
│   ├── config.py
│   ├── preprocess.py
│   ├── build_index.py
│   ├── query_engine.py
│
├── .env
├── requirements.txt
└── README.md
```

---

# 📁 File-by-File Explanation

---

## 1️⃣ `config.py`

Central configuration file.

Defines:
- Dataset path
- Gemini LLM model
- Gemini embedding model
- API key loading
- Retrieval parameters
- Index row limits

Why centralized config?
- Clean separation of logic and settings
- Easier scaling
- Professional project structure

---

## 2️⃣ `preprocess.py`

Handles:

### ✔ Data Cleaning
- Removes cancelled invoices
- Removes invalid quantities
- Drops missing CustomerID
- Fixes data types

### ✔ Feature Engineering
- Revenue column
- YearMonth column
- Datetime conversion

### ✔ KPI Computation
- Total revenue
- Top country by revenue
- Monthly revenue aggregation

Why this step?

LLMs cannot work directly with raw tabular noise.
We must:
- Clean
- Structure
- Engineer meaningful business features

This shows real Data Analyst thinking.

---

## 3️⃣ `build_index.py`

Core RAG builder.

### Step 1 — Convert rows into semantic documents

Each row becomes:

```
Invoice 12345 from UK on 2011-12-01.
Product: White Mug.
Quantity: 12.
Unit Price: 2.55.
Revenue: 30.60.
Customer ID: 17850.
```

Why?

LLMs understand natural language better than raw tables.

---

### Step 2 — Build Vector Index

Uses:

- `SimpleVectorStore` (in-memory)
- Gemini embeddings
- VectorStoreIndex

Why SimpleVectorStore?

- No external DB required
- Zero configuration
- Clean for portfolio use
- Avoids deployment complexity

---

## 4️⃣ `query_engine.py`

Implements **Hybrid Query Routing**.

We detect query type:

### Numeric Query
Example:
- "What is total revenue?"
- "Which country generated highest revenue?"

→ Routed to `PandasQueryEngine`
→ Executes actual dataframe computation

---

### Semantic Query
Example:
- "Describe purchasing behavior in UK"
- "What kind of products are popular?"

→ Routed to RAG retriever
→ Retrieves relevant invoice rows
→ LLM generates contextual explanation

---

This hybrid architecture is powerful because:

- Numeric accuracy comes from Pandas
- Contextual reasoning comes from RAG
- We avoid hallucinated numbers

This is production-level thinking.

---

## 5️⃣ `main.py`

Orchestrates entire pipeline.

Steps:

1. Initialize Gemini
2. Load dataset
3. Preprocess data
4. Compute KPIs
5. Create documents
6. Build vector index
7. Build query engines
8. Accept user queries
9. Route intelligently
10. Return response

This file ties everything together.

---

# 🧠 Why This Approach Was Chosen

### 1️⃣ Demonstrates Real-World Pipeline

Not just LLM calls.
Not just Pandas.
But orchestration between:

- Data Engineering
- Retrieval
- Embeddings
- Query routing
- Generation

---

### 2️⃣ Shows Understanding of RAG

Instead of blindly using an LLM,
we:

- Convert structured data → semantic documents
- Index embeddings
- Retrieve relevant context
- Inject context into LLM

This prevents hallucination and improves reasoning.

---

### 3️⃣ Hybrid Analytics = Edge Over Competitors

Most candidates:

- Either use Pandas
- Or use LLM

Very few combine both properly.

This project demonstrates:

✔ Controlled LLM usage  
✔ Numeric reliability  
✔ Semantic intelligence  
✔ Engineering discipline  

---

### 4️⃣ Modular Design

Each file has single responsibility.

This shows:

- Clean code practices
- Separation of concerns
- Scalable design

---

# 💡 Example Queries

Numeric:

- "What is the total revenue?"
- "Which country generated the highest revenue?"
- "Show monthly revenue trends."

Semantic:

- "Describe UK customer purchasing patterns."
- "What type of products sell most frequently?"
- "What insights can you derive from recent transactions?"

---

# 🔥 Technologies Used

- Python
- Pandas
- LlamaIndex
- Gemini API
- Vector Embeddings
- RAG Architecture
- dotenv
- Modular project structure

---

# ⚙️ Setup Instructions

### 1️⃣ Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate
```

### 2️⃣ Install Dependencies

```
pip install -r requirements.txt
```

### 3️⃣ Create `.env`

```
GOOGLE_API_KEY=your_api_key_here
```

### 4️⃣ Run

```
python src/main.py
```

---

# 📈 Business Use Cases

This architecture can be extended for:

- Customer behavior analysis
- Business intelligence dashboards
- Financial audit assistants
- Sales analytics copilots
- Automated reporting agents
- Executive decision support systems

---

# 🏆 Why This Is Resume-Worthy

This project demonstrates:

- Understanding of LLM internals
- Knowledge of embedding pipelines
- RAG architecture implementation
- Hybrid data systems
- Error handling & debugging
- Quota management awareness
- Clean modular engineering

This goes far beyond:

"Built a chatbot."

This shows:

"I can design AI systems."

---

# 🚀 Future Improvements

- Add Streamlit UI
- Add evaluation metrics
- Add caching layer
- Add persistent vector DB (FAISS / Chroma)
- Add batch embedding pipeline
- Add monitoring + logging
- Add API endpoint for production

---

# 📌 Final Summary

This project transforms structured retail data into an intelligent conversational analytics system using:

- Data preprocessing
- Semantic indexing
- Hybrid query routing
- Gemini LLM reasoning
- Modular pipeline design

It demonstrates real-world LLM orchestration and applied AI engineering suitable for Data Analyst, AI Engineer, or GenAI roles.

---

**Author:** Krishna  
**Focus:** Data + AI + LLM Systems  
**Architecture:** Hybrid RAG + Structured Analytics  
