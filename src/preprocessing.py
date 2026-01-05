
import re


def clean_text(text: str) -> str:
    
    # Convert to lowercase
    text = text.lower()

    # Remove URLs
    text = re.sub(r"http\S+|www\S+", "", text)

    # Remove extra whitespace
    text = re.sub(r"\s+", " ", text).strip()

    return text
"""
    Perform minimal text cleaning suitable for cognitive analysis.

    Steps:
    - Convert text to lowercase
    - Remove URLs
    - Normalize extra whitespace
    - Preserve punctuation and negations

    Parameters:
        text (str): Raw input text

    Returns:
        str: Cleaned text
    """