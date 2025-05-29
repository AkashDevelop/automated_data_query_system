from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline , logging
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_community.llms import HuggingFacePipeline
import re
import os

os.environ["TRANSFORMERS_VERBOSITY"] = "error"
logging.set_verbosity_error()

# Initialize phi-2 model 
MODEL = "microsoft/phi-2"
_tok = AutoTokenizer.from_pretrained(MODEL, trust_remote_code=True)
_mod = AutoModelForCausalLM.from_pretrained(
    MODEL,
    device_map={"": "cpu"},
    torch_dtype="auto",
    trust_remote_code=True
)
text_gen = pipeline(
    "text-generation",
    model=_mod,
    tokenizer=_tok,
    max_new_tokens=150,
    do_sample=False,
    pad_token_id=_tok.eos_token_id,
    return_full_text=False
)

def generate_mongodb_query(req: str) -> str:
    prompt = f"""
Generate a MongoDB find() query as valid JSON. Follow rules:
1. Use only these fields: ProductID, ProductName, Category, Price, Rating, ReviewCount, Stock, Discount, Brand, LaunchDate
2. For numbers: Use operators like {{"$gt": 50}}
3. For text: Use exact matches {{"Brand": "Nike"}}
4. For dates: Use ISO format {{"LaunchDate": {{"$gt": "2022-01-01"}}}}
5. For multiple conditions: Use {{"$and": [condition1, condition2]}}, or {{"$or": [ ... ]}}
6. Output ONLY the JSON object, no extra text.

User request: "{req}"
Query JSON:
"""
    out = text_gen(prompt)[0]["generated_text"]
    m = re.search(r"\{.*\}", out, re.DOTALL)
    return m.group(0) if m else "{}"


import re
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

# Initialize phi-2 model
MODEL = "microsoft/phi-2"
_tok = AutoTokenizer.from_pretrained(MODEL, trust_remote_code=True)
_mod = AutoModelForCausalLM.from_pretrained(
    MODEL,
    device_map={"": "cpu"},
    torch_dtype="auto",
    trust_remote_code=True
)
text_gen = pipeline(
    "text-generation",
    model=_mod,
    tokenizer=_tok,
    max_new_tokens=150,
    do_sample=False
)

def generate_mongodb_query(req: str) -> str:
    prompt = f"""
Generate a MongoDB find() query as valid JSON. Follow these rules:
1. Use only these fields: ProductID, ProductName, Category, Price, Rating, ReviewCount, Stock, Discount, Brand, LaunchDate
2. For numbers: Use operators like {{"$gt": 50}}
3. For text: Use exact matches {{"Brand": "Nike"}}
4. For dates: Use ISO format {{"LaunchDate": {{"$gt": "2022-01-01"}}}}
5. For multiple conditions: Use {{"$and": [condition1, condition2]}}, or {{"$or": [ ... ]}}
6. Output ONLY the JSON object, no extra text.

User request: "{req}"
Query JSON:
"""
    out = text_gen(prompt)[0]["generated_text"]
    m = re.search(r"\{.*\}", out, re.DOTALL)
    return m.group(0) if m else "{}"
