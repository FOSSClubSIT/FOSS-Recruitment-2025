"""
Streamlit News Summarizer & Sentiment Analyzer
----------------------------------------------
This app extracts text from a news article URL, summarizes it, 
and analyzes sentiment — with a futuristic background.
"""
    
import streamlit as st
from transformers import pipeline
from newspaper import Article
import base64

# Load Hugging Face models (local, no API keys needed)
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
sentiment_analyzer = pipeline("sentiment-analysis", 
                              model="distilbert-base-uncased-finetuned-sst-2-english")

def set_background(image_file):
    """Reads local image and encodes it as base64 to set as background in Streamlit."""
    with open("D:\\VScodefiles\\360_F_492391117_bsAteaWt7I9gCAJY1Mt3QXXxdLXE2Nzq.jpg", "rb") as file:
        encoded = base64.b64encode(file.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded}");
            background-size: cover;
            background-attachment: fixed;
        }}
        .main-title {{
            color: white;
            text-shadow: 2px 2px 5px black;
        }}
        .card {{
            background: rgba(0, 0, 0, 0.6);
            padding: 20px;
            border-radius: 15px;
            color: white;
            box-shadow: 0px 0px 15px rgba(0,0,0,0.8);
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

def extract_text(url: str) -> str:
    """Extracts article text from a URL using newspaper3k."""
    article = Article(url)
    article.download()
    article.parse()
    return article.text