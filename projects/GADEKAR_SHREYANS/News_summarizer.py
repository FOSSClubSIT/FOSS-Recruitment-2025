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

