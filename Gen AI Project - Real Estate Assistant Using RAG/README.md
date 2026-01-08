<div align="center">

# 🏠 Real Estate Intel-Agent
**High-Performance RAG Pipeline for Automated Property Market Analysis**

[![Python](https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![LangChain](https://img.shields.io/badge/LangChain-white?style=for-the-badge&logo=chainlink&logoColor=black)](https://langchain.com/)
[![VectorDB](https://img.shields.io/badge/VectorDB-Chroma-orange?style=for-the-badge)](https://www.trychroma.com/)
[![Model](https://img.shields.io/badge/LLM-Groq--GPT--OSS-green?style=for-the-badge)](https://groq.com/)

---

[Explore Demo](#-usage) • [Report Bug](https://github.com/Kalyan9639/langchain-and-langgraph-series/issues) • [Request Feature](https://github.com/your-username/repo/issues)

</div>

## 📖 Overview

**Real Estate Intel-Agent** is a sophisticated Retrieval-Augmented Generation (RAG) platform designed to synthesize vast amounts of real estate web data into actionable insights. By combining **IBM's Granite Embeddings** with the extreme inference speed of **Groq**, this agent allows users to query complex property blogs, tax laws, and market trends with zero-latency response times and full source transparency.

### 🌟 Key Capabilities
- **Dynamic Web Ingestion**: Parallel processing of multiple property-related URLs using `UnstructuredURLLoader`.
- **Hybrid Context Retrieval**: Semantic search optimized via `RecursiveCharacterTextSplitter` for high-context retention.
- **Embedded Intelligence**: Leverages `ibm-granite/granite-embedding-small-english-r2` for superior semantic mapping in the real estate domain.
- **Source Attribution**: Every response is back-linked to the source document, ensuring data integrity and auditability.

---

## 🏗️ System Architecture

The pipeline is engineered for modularity and scalability:

1.  **Ingestion Layer**: Scrapes raw HTML and cleans data using the `Unstructured` framework.
2.  **Transformation Layer**: Implements a recursive splitting strategy ($Chunk Size: 1000$, $Overlap: 200$) to maintain semantic continuity.
3.  **Vector Store Layer**: Persists embeddings in a local `Chroma` instance for rapid retrieval without redundant API calls.
4.  **Inference Layer**: Orchestrates a `ChatPromptTemplate` chain via **Groq** to generate context-grounded responses.

---

## 🛠️ Technical Specifications

| Component | Implementation |
| :--- | :--- |
| **Embeddings** | `ibm-granite/granite-embedding-small-english-r2` |
| **LLM Engine** | `openai/gpt-oss-20b` (via Groq Cloud) |
| **Vector Database** | ChromaDB (Local Persistence) |
| **Framework** | LangChain Expression Language (LCEL) |
| **Concurrency** | Python Generator-based Status Streaming |

---

## 🚀 Getting Started

### Prerequisites
- Python 3.9+
- A [Groq Cloud](https://console.groq.com/) API Key

### Installation

1. **Clone the repository**
   ```bash
   git clone [https://github.com/your-username/real-estate-intel-agent.git](https://github.com/your-username/real-estate-intel-agent.git)
   cd real-estate-intel-agent
   ```


