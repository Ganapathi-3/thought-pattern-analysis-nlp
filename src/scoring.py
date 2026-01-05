"""
scoring.py

This module converts extracted cognitive features into
interpretable thought-pattern scores.
"""

from typing import Dict


def clamp(value: float, min_value: float = 0.0, max_value: float = 1.0) -> float:
    """Ensure score stays within range."""
    return max(min_value, min(value, max_value))


def score_thought_patterns(features: Dict[str, float]) -> Dict[str, Dict[str, float]]:
    """
    Generate thought-pattern scores from cognitive features.

    Parameters:
        features (Dict[str, float]): Output from feature_engineering

    Returns:
        Dict: Thought pattern scores with explanations
    """

    # Absolutist vs Balanced
    absolutist_score = clamp(features["absolutist_ratio"] * 3)
    balanced_score = clamp(features["balanced_ratio"] * 3)

    # Emotional vs Rational
    emotional_score = clamp(features["emotion_ratio"] * 3)
    rational_score = clamp(features["rational_ratio"] * 3)

    # Analytic vs Holistic (proxy using sentence length & rationality)
    analytic_score = clamp(
        (features["rational_ratio"] * 2) +
        (features["avg_sentence_length"] / 20)
    )
    holistic_score = clamp(1 - analytic_score)

    # Concrete vs Abstract (simple proxy using pronouns & rationality)
    concrete_score = clamp(features["first_person_ratio"] * 2)
    abstract_score = clamp(
        (features["rational_ratio"] + features["collective_person_ratio"])
    )

    return {
        "Analytic_vs_Holistic": {
            "analytic": analytic_score,
            "holistic": holistic_score
        },
        "Absolutist_vs_Balanced": {
            "absolutist": absolutist_score,
            "balanced": balanced_score
        },
        "Emotional_vs_Rational": {
            "emotional": emotional_score,
            "rational": rational_score
        },
        "Concrete_vs_Abstract": {
            "concrete": concrete_score,
            "abstract": abstract_score
        }
    }
