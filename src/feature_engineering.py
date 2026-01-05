"""
feature_engineering.py

This module extracts interpretable cognitive and linguistic features
from text that are useful for thought pattern analysis.
"""

import re
from typing import Dict


# Lexicons (simple and interpretable)


ABSOLUTIST_WORDS = {
    "always", "never", "nothing", "everything", "everyone", "no one",
    "completely", "totally", "entirely", "forever"
}

BALANCED_WORDS = {
    "sometimes", "maybe", "often", "likely", "possibly",
    "generally", "depends", "usually"
}

EMOTION_WORDS = {
    "sad", "happy", "angry", "frustrated", "excited",
    "afraid", "worried", "hurt", "depressed"
}

RATIONAL_WORDS = {
    "because", "therefore", "reason", "logic",
    "evidence", "data", "analysis", "result"
}

FIRST_PERSON = {"i", "me", "my", "mine"}
COLLECTIVE_PERSON = {"we", "us", "our", "they", "them"}


# Helper functions


def tokenize(text: str):
    """Simple whitespace tokenizer."""
    return re.findall(r"\b\w+\b", text.lower())



# Feature extraction


def extract_cognitive_features(text: str) -> Dict[str, float]:
    """
    Extract interpretable cognitive features from text.

    Parameters:
        text (str): Cleaned input text

    Returns:
        Dict[str, float]: Feature name -> value
    """
    tokens = tokenize(text)
    total_tokens = len(tokens) if tokens else 1

    absolutist_count = sum(1 for t in tokens if t in ABSOLUTIST_WORDS)
    balanced_count = sum(1 for t in tokens if t in BALANCED_WORDS)
    emotion_count = sum(1 for t in tokens if t in EMOTION_WORDS)
    rational_count = sum(1 for t in tokens if t in RATIONAL_WORDS)

    first_person_count = sum(1 for t in tokens if t in FIRST_PERSON)
    collective_person_count = sum(1 for t in tokens if t in COLLECTIVE_PERSON)

    features = {
        "absolutist_ratio": absolutist_count / total_tokens,
        "balanced_ratio": balanced_count / total_tokens,
        "emotion_ratio": emotion_count / total_tokens,
        "rational_ratio": rational_count / total_tokens,
        "first_person_ratio": first_person_count / total_tokens,
        "collective_person_ratio": collective_person_count / total_tokens,
        "avg_sentence_length": total_tokens / max(1, text.count(".") + text.count("!") + text.count("?"))
    }

    return features
