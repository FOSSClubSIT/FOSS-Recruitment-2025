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

def chunk_text(text, max_tokens=200):
    """Splits long text into smaller chunks for summarization."""
    words = text.split()
    for i in range(0, len(words), max_tokens):
        yield " ".join(words[i:i + max_tokens])

def summarize_text(text: str) -> str:
    """Summarizes long text in chunks and returns a final summary."""
    chunks = list(chunk_text(text))
    summaries = []
    for chunk in chunks:
        input_len = len(chunk.split())
        max_len = min(120, int(input_len * 0.8))
        min_len = min(50, int(input_len * 0.4))
        summary = summarizer(chunk, max_length=max_len, min_length=min_len, do_sample=False)
        summaries.append(summary[0]['summary_text'])
    final_summary = summarizer(" ".join(summaries), max_length=100, min_length=50, do_sample=False)
    return final_summary[0]['summary_text']

def analyze_sentiment(text: str) -> str:
    """Analyzes sentiment of text."""
    result = sentiment_analyzer(text)[0]
    return f"{result['label']} (confidence: {result['score']:.2f})"

set_background("360_F_492391117_bsAteaWt7I9gCAJY1Mt3QXXxdLXE2Nzq.jpg")  # your background image

st.markdown("<h1 class='main-title'>📰 News Summarizer & Sentiment Analyzer</h1>", unsafe_allow_html=True)
st.markdown("<p style='color:white;'>Paste any news article URL below and let AI do the rest!</p>", unsafe_allow_html=True)

url = st.text_input("Enter News Article URL:")

if st.button("Summarize & Analyze"):
    if url:
        try:
            with st.spinner("Extracting article..."):
                article_text = extract_text(url)

            st.markdown("<div class='card'><h3>Extracted Article</h3></div>", unsafe_allow_html=True)
            st.write(article_text[:500] + "...")

            with st.spinner("📝 Generating summary..."):
                summary = summarize_text(article_text)
            st.markdown("<div class='card'><h3>Summary</h3></div>", unsafe_allow_html=True)
            st.success(summary)

            with st.spinner("🔍 Analyzing sentiment..."):
                sentiment = analyze_sentiment(summary)
            st.markdown("<div class='card'><h3>Sentiment</h3></div>", unsafe_allow_html=True)
            st.info(sentiment)

        except Exception as e:
            st.error(f"⚠️ Error: {e}")
    else:
        st.warning("Please enter a valid URL.")