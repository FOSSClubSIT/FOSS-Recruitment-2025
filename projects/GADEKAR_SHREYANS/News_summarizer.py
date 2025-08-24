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