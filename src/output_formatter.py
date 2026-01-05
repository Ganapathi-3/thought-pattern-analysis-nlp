"""
output_formatter.py

This module converts numerical thought-pattern scores
into human-readable interpretations.
"""

from typing import Dict


def label_score(score: float) -> str:
    """Convert numeric score to qualitative label."""
    if score >= 0.7:
        return "High"
    elif score >= 0.4:
        return "Medium"
    else:
        return "Low"


def format_thought_patterns(scores: Dict[str, Dict[str, float]]) -> Dict[str, Dict[str, str]]:
    """
    Convert thought pattern scores into interpretable labels and explanations.

    Parameters:
        scores (dict): Output from scoring.py

    Returns:
        dict: Human-readable interpretation
    """

    formatted_output = {}

    for pattern, values in scores.items():
        interpretation = {}
        for k, v in values.items():
            interpretation[k] = label_score(v)
        formatted_output[pattern] = interpretation

    return formatted_output
