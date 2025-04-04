# generator.py (新API格式)
import os
from openai import OpenAI
from config import OPENAI_API_KEY, MODEL_NAME, PROMPT_FOLDER

client = OpenAI(api_key=OPENAI_API_KEY)

def load_prompt(prompt_name):
    with open(os.path.join(PROMPT_FOLDER, prompt_name), "r", encoding="utf-8") as f:
        return f.read()

def generate_strategy(prompt_name="basic_trend.txt"):
    prompt = load_prompt(prompt_name)
    print("[📤] Prompt内容：", prompt[:100], "...")

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": "你是一个交易策略工程师"},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    return response.choices[0].message.content
