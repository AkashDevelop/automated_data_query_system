Automated Data Query & Retrieval System

What I Built

A Python tool that:

Loads product data from CSV into MongoDB.

Takes your natural-language question and asks a local LLM (Phi-2) to write a MongoDB query.

Runs that query and either shows results in the console or saves them as a CSV.

Challenges We Faced

Module Imports: Had to learn running python -m src.main from project root to fix import errors.

Big Model Downloads: Original Phi-2 shards (5GB) were too heavy; switched to offline, CPU-only loading and pointed at a cache.

Prompt Braces: LangChain templates misinterpreted {}—we switched to f-strings with escaped braces.

bitsandbytes Errors: Backend didn’t support 4-bit on our machine, so we dropped quant flags.

Quick Start

Install requirements: pip install -r requirements.txt

Make sure MongoDB is running locally.

Run:

python -m src.main

Ask:

E.g. “Find products with rating below 4.5 and brand Nike.”

Choose to show on screen or save to outputs/.

Enjoy your offline, LLM-driven query assistant!

Security: All LLM output is regex-validated as JSON before DB execution.

Scalability: Could plug in multiple CSVs or a UI frontend.

Model swap: To reduce disk footprint, swap to Smaller GGUF models (TinyLlama) by changing MODEL in llm_query_generator.py.

LangChain Update: Replace deprecated HuggingFacePipeline with langchain-huggingface for future-proofing.

