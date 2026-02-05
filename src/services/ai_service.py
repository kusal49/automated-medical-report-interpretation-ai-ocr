from groq import Groq
from config.app_config import AppConfig

from config.prompts import (
    MASTER_PROMPT,
    REPORT_PARSER_PROMPT,
    INSIGHT_AGENT_PROMPT,
    LIFESTYLE_AGENT_PROMPT,
    SAFETY_AGENT_PROMPT,
)

client = Groq(api_key=AppConfig.GROQ_API_KEY)

MODELS = [
    "meta-llama/llama-4-maverick-17b-128e-instruct",
    "llama-3.3-70b-versatile",
    "llama-3.1-8b-instant",
    "llama3-70b-8192"
]

def call_llm(system_prompt, user_content, model):
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_content}
        ],
        temperature=0.3
    )
    return response.choices[0].message.content


def run_with_fallback(system_prompt, user_content):
    for model in MODELS:
        try:
            return call_llm(system_prompt, user_content, model)
        except Exception as e:
            print(f"Model {model} failed: {e}")
    raise RuntimeError("All models failed")
