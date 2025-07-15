"""
LLM processor for summarizing or describing input text using OpenAI GPT models.
"""

import os
from typing import List
from openai import OpenAI
from app.utils import chunk_text
from dotenv import load_dotenv

# Initialize OpenAI client
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def transform_text(raw_text: str, mode: str = "summary") -> List[str]:
    """
    Transform input text using GPT in the specified mode.

    Args:
        raw_text: Full input text.
        mode: 'summary' or 'description'.

    Returns:
        List of transformed text chunks.
    """
    if mode not in ["summary", "description"]:
        raise ValueError("Invalid mode. Use 'summary' or 'description'.")

    chunks = chunk_text(raw_text)
    results = []

    for chunk in chunks:
        if not chunk.strip():
            continue

        prompt = build_prompt(chunk, mode)
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant that transforms text."},
                    {"role": "user", "content": prompt}
                ]
            )
            result = response.choices[0].message.content.strip()
            results.append(result)
        except Exception as e:
            results.append(f"[ERROR]: {str(e)}")

    return results


def build_prompt(text: str, mode: str) -> str:
    """
    Generate prompt for LLM based on mode.

    Args:
        text: Input chunk.
        mode: 'summary' or 'description'.

    Returns:
        Prompt string for GPT.
    """
    if mode == "summary":
        return f"Summarize the following text:\n{text}"
    else:
        return f"Describe the following text:\n{text}"
