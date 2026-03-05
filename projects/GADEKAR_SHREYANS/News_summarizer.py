"""
Streamlit News Summarizer & Sentiment Analyzer
----------------------------------------------
This app extracts text from a news article URL, summarizes it, 
and analyzes sentiment, generates wordcloud, and also pdf — with a futuristic background.
"""

import torch    
import streamlit as st
from transformers import pipeline
from newspaper import Article
import base64
import requests
from bs4 import BeautifulSoup
import spacy
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from io import BytesIO
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from docx import Document
import subprocess
import sys
import os

# ------------------- Load Models -------------------
summarizer = pipeline("summarization", model="facebook/bart-large-cnn", device=-1)
sentiment_pipeline = pipeline("sentiment-analysis", device=-1)
topic_classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli", device=-1)
emotion_classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", device=-1)
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    subprocess.run([sys.executable, "-m", "spacy", "download", "en_core_web_sm"])
    nlp = spacy.load("en_core_web_sm")

def set_background(image_file):
    """Reads local image and encodes it as base64 to set as background in Streamlit."""
    file_path = os.path.join(os.path.dirname(__file__), image_file)
    with open(file_path, "rb") as file:
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

def extract_text_from_url(url):
    try:
        r = requests.get(url, timeout=10)
        soup = BeautifulSoup(r.text, "html.parser")
        paragraphs = soup.find_all("p")
        return " ".join([p.get_text() for p in paragraphs])
    except Exception as e:
        return str(e)

def generate_wordcloud(text):
    wc = WordCloud(width=800, height=400, background_color="black").generate(text)
    fig, ax = plt.subplots()
    ax.imshow(wc, interpolation="bilinear")
    ax.axis("off")
    return fig

def generate_pdf(text, summary, sentiment, topics, entities, emotions):
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer)
    styles = getSampleStyleSheet()
    flow = []
    flow.append(Paragraph("📑 News Analysis Report", styles['Title']))
    flow.append(Spacer(1, 12))
    flow.append(Paragraph(f"<b>Extracted Text:</b> {text}", styles['Normal']))
    flow.append(Spacer(1, 12))
    flow.append(Paragraph(f"<b>Summary:</b> {summary}", styles['Normal']))
    flow.append(Spacer(1, 12))
    flow.append(Paragraph(f"<b>Sentiment:</b> {sentiment}", styles['Normal']))
    flow.append(Spacer(1, 12))
    flow.append(Paragraph(f"<b>Topics:</b> {topics}", styles['Normal']))
    flow.append(Spacer(1, 12))
    flow.append(Paragraph(f"<b>Entities:</b> {entities}", styles['Normal']))
    flow.append(Spacer(1, 12))
    flow.append(Paragraph(f"<b>Emotions:</b> {emotions}", styles['Normal']))
    doc.build(flow)
    buffer.seek(0)
    return buffer

# ------------------- Streamlit UI -------------------
set_background("360_F_492391117_bsAteaWt7I9gCAJY1Mt3QXXxdLXE2Nzq.jpg")

st.markdown("<h1 class='main-title'>📰 News Summarizer & Sentiment Analyzer</h1>", unsafe_allow_html=True)
st.markdown("<p style='color:white;'>Paste any news article URL below and let AI do the rest!</p>", unsafe_allow_html=True)

url = st.text_input("Enter a news article URL")

if url:
    article_text = extract_text_from_url(url)
    if len(article_text) > 100:
        with st.spinner("Analyzing..."):
            # Summarization
            summary = summarizer(article_text[:1000], max_length=150, min_length=50, do_sample=False)[0]['summary_text']
            
            # Sentiment
            sentiment = sentiment_pipeline(article_text[:512])[0]['label']
            
            # Topic Classification
            candidate_labels = ["Politics", "Sports", "Technology", "Health", "Entertainment", "Crime"]
            topics = topic_classifier(article_text[:512], candidate_labels)['labels'][0]
            
            # NER
            doc = nlp(article_text[:512])
            entities = ", ".join([f"{ent.text} ({ent.label_})" for ent in doc.ents])
            
            # Emotions
            emotions = emotion_classifier(article_text[:512])[0]['label']
            
            # Display
            st.subheader("Extracted Text")
            st.write(article_text[:1000] + "...")
            
            st.subheader("Summary")
            st.write(summary)
            
            st.subheader("Sentiment")
            st.success(sentiment)
            
            st.subheader("Topic Classification")
            st.info(topics)
            
            st.subheader("Named Entities")
            st.warning(entities if entities else "No significant entities found")
            
            st.subheader("Emotion Detection")
            st.success(emotions)
            
            st.subheader("Word Cloud")
            st.pyplot(generate_wordcloud(article_text))
            
            # Download Reports
            st.subheader("Download Reports")
            pdf_buf = generate_pdf(article_text, summary, sentiment, topics, entities, emotions)
            
            st.download_button("Download PDF Report", pdf_buf, "report.pdf", "application/pdf")
    else:
        st.error("Could not extract enough text from the URL.")