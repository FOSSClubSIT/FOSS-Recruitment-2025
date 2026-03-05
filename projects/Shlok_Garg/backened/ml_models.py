import os
import logging
from pathlib import Path
from dotenv import load_dotenv

# ML Libraries
from transformers import pipeline, AutoTokenizer, AutoModelForTokenClassification
from sentence_transformers import SentenceTransformer
from keybert import KeyBERT
import torch
import spacy

ROOT_DIR = Path(__file__).parent
load_dotenv(ROOT_DIR / '.env')

# Initialize ML Models (Global to avoid reloading)
print("Loading enhanced ML models...")
try:
    # Get Hugging Face token from environment
    huggingface_token = os.environ.get("HUGGINGFACE_TOKEN")
    
    # Primary NER Model - Better accuracy (dbmdz model ~1.3GB)
    print("Loading primary NER model...")
    ner_tokenizer = AutoTokenizer.from_pretrained("dbmdz/bert-large-cased-finetuned-conll03-english", token=huggingface_token)
    ner_model = AutoModelForTokenClassification.from_pretrained("dbmdz/bert-large-cased-finetuned-conll03-english", token=huggingface_token)
    ner_pipeline = pipeline("ner", 
                           model=ner_model, 
                           tokenizer=ner_tokenizer, 
                           aggregation_strategy="simple",
                           device=-1)  # CPU only
    
    # Fallback spaCy model for faster processing
    print("Loading spaCy model...")
    try:
        spacy_nlp = spacy.load("en_core_web_sm")
    except OSError:
        print("spaCy model not found, using transformers only")
        spacy_nlp = None
    
    # Better Sentence Transformer for embeddings (~420MB)
    print("Loading sentence transformer...")
    embedding_model = SentenceTransformer('sentence-transformers/all-mpnet-base-v2', token=huggingface_token)
    
    # Job-specific model for better job matching (~440MB)
    print("Loading job-specific model...")
    try:
        job_model = SentenceTransformer('jjzha/jobbert-base-cased', token=huggingface_token)
    except:
        print("JobBERT not available, using main embedding model")
        job_model = embedding_model
    
    # KeyBERT for keyword extraction
    kw_model = KeyBERT(model=embedding_model)
    
    # Resume classification pipeline
    print("Loading resume classification model...")
    try:
        resume_classifier = pipeline("text-classification", 
                                   model="microsoft/DialoGPT-small", 
                                   token=huggingface_token)
    except:
        print("Resume classifier not available, using NER pipeline")
        resume_classifier = None
    
    print("✅ All enhanced ML models loaded successfully!")
    print(f"Total models loaded: {sum([bool(x) for x in [ner_pipeline, embedding_model, kw_model, spacy_nlp, job_model]])}")
    
except Exception as e:
    print(f"❌ Error loading models: {e}")
    ner_pipeline = None
    embedding_model = None
    kw_model = None
    spacy_nlp = None
    job_model = None
    resume_classifier = None
