"""
Utility functions for text processing.
"""

from typing import List

def chunk_text(text: str, max_lines: int = 50) -> List[str]:
    """
    Splits text into smaller chunks based on line count.

    Args:
        text: The full input text.
        max_lines: Number of lines per chunk.

    Returns:
        List of text chunks.
    """
    lines = text.splitlines()
    chunks = []

    for i in range(0, len(lines), max_lines):
        chunk = "\n".join(lines[i:i + max_lines]).strip()
        if chunk:
            chunks.append(chunk)

    return chunks
