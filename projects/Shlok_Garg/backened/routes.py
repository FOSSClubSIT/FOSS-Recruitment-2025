from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from fastapi.responses import JSONResponse
from typing import Optional
import io
import logging

from models import AnalysisResult, HealthCheck
from ml_models import ner_pipeline, embedding_model, kw_model, spacy_nlp, job_model, resume_classifier
from utils import (
    extract_text_from_pdf, 
    extract_entities, 
    extract_keywords, 
    calculate_match_score,
    calculate_job_profile_score,
    find_missing_keywords
)

# Create a router with the /api prefix
api_router = APIRouter(prefix="/api")

logger = logging.getLogger(__name__)

# API Routes
@api_router.get("/", response_model=HealthCheck)
async def root():
    """Health check endpoint"""
    models_loaded = all([ner_pipeline, embedding_model, kw_model])
    total_models = sum([bool(x) for x in [ner_pipeline, embedding_model, kw_model, spacy_nlp, job_model, resume_classifier]])
    
    return HealthCheck(
        status="healthy",
        models_loaded=models_loaded,
        message=f"Resume Analyzer API is running with {total_models}/6 enhanced models loaded"
    )

@api_router.post("/analyze", response_model=AnalysisResult)
async def analyze_resume(
    resume: UploadFile = File(..., description="Resume PDF file (max 15MB)"),
    job_description: Optional[str] = Form(None, description="Job description text (optional)")
):
    """
    Analyze resume PDF and optionally match against job description
    """
    # Validate file size (15MB limit)
    if resume.size > 15 * 1024 * 1024:
        raise HTTPException(status_code=400, detail="File size exceeds 15MB limit")
    
    # Validate file type
    if not resume.filename.lower().endswith('.pdf'):
        raise HTTPException(status_code=400, detail="Only PDF files are supported")
    
    try:
        # Read PDF content
        pdf_content = await resume.read()
        pdf_file = io.BytesIO(pdf_content)
        
        # Extract text from PDF
        resume_text = extract_text_from_pdf(pdf_file)
        
        if not resume_text.strip():
            raise HTTPException(status_code=400, detail="No text could be extracted from the PDF")
        
        # Extract entities
        entities = extract_entities(resume_text)
        
        # Extract keywords from resume
        resume_keywords = extract_keywords(resume_text)
        
        # Initialize JD-related variables
        jd_keywords = []
        missing_keywords = []
        match_score = 0.0
        
        # Process job description if provided
        if job_description and job_description.strip():
            jd_keywords = extract_keywords(job_description)
            missing_keywords = find_missing_keywords(resume_keywords, jd_keywords)
            match_score = calculate_match_score(resume_text, job_description)
        
        # Generate job profile analysis (new feature)
        job_profile_analysis = calculate_job_profile_score(resume_text, entities, resume_keywords)
        
        result = AnalysisResult(
            entities=entities,
            match_score=match_score,
            resume_keywords=resume_keywords,
            jd_keywords=jd_keywords,
            missing_keywords=missing_keywords,
            resume_text=resume_text[:500] + "..." if len(resume_text) > 500 else resume_text,
            job_profile_analysis=job_profile_analysis
        )
        
        return result
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error in analyze_resume: {e}")
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")
