# 🤖 Automated Data Query & Retrieval System

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![MongoDB](https://img.shields.io/badge/MongoDB-%23117A45.svg?logo=mongodb&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-%23734dd7.svg?logo=langchain&logoColor=white)
![License](https://img.shields.io/badge/license-MIT-green)

A lightweight, offline-capable Python tool for **natural language database querying** using MongoDB and a local LLM.

---

## 🚀 What I Built

A Python-based assistant that:

- 📦 Loads product data from CSV into MongoDB.
- 🧠 Uses a local LLM (Phi-2) to generate MongoDB queries from your **natural-language questions**.
- 🖥️ Executes the query and either:
  - Displays results in the console
  - Saves results as a CSV file

---

## 🧗 Challenges I Faced

- 🧩 **Module Imports**  
  Resolved import errors by running `python -m src.main` from the project root.

- 💾 **Model Size**  
  Phi-2 shards (~5GB) were too heavy — switched to CPU-only loading from local cache.

- 🧵 **Prompt Formatting**  
  LangChain misinterpreted `{}` in templates — replaced with `f-strings` and escaped braces.

- ⚙️ **bitsandbytes Errors**  
  Our machine didn't support 4-bit quant — removed quantization flags for compatibility.

---

## ⚡ Quick Start

1. **Install dependencies:**

   ```bash
   pip install -r requirements.txt

2. **Start MongoDB locally**
3. **Run the main module:**
     ```bash
   python -m src.main
5. **Ask questions like:**
       “Find products with rating below 4.5 and brand Nike.”



