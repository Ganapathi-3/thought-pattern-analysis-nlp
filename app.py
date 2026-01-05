import streamlit as st
import pandas as pd

from src.preprocessing import clean_text
from src.feature_engineering import extract_cognitive_features
from src.scoring import score_thought_patterns
from src.output_formatter import format_thought_patterns


st.set_page_config(page_title="Thought Pattern Analysis", layout="centered")

st.title(" Thought Pattern Analysis from Text")

st.write(
    "Enter a piece of text below to analyze underlying cognitive thought patterns."
)

# Text input box
user_text = st.text_area(
    "Input Text",
    placeholder="Type or paste your text here...",
    height=150
)

# Button
if st.button("Analyze Thought Patterns"):

    if user_text.strip() == "":
        st.warning("Please enter some text before analyzing.")
    else:
        # Run pipeline
        cleaned = clean_text(user_text)
        features = extract_cognitive_features(cleaned)
        scores = score_thought_patterns(features)
        readable = format_thought_patterns(scores)

        # Convert to table
        df = pd.DataFrame(readable).T

        st.subheader(" Analysis Result")
        st.dataframe(df)

        # Simple bar chart
        level_map = {"Low": 1, "Medium": 2, "High": 3}
        plot_df = df.replace(level_map)

        st.subheader(" Visualization")
        st.bar_chart(plot_df)

        st.info(
            "This tool is for educational and analytical purposes only. "
            "It is not a psychological or medical diagnosis."
        )
