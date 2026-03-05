from pydantic import BaseModel
from typing import List, Optional, Dict, Any

class JobProfileScore(BaseModel):
    detected_role: str
    role_confidence: float
    overall_score: float
    category_scores: Dict[str, Dict[str, Any]]
    recommendations: List[str]

class AnalysisResult(BaseModel):
    entities: Dict[str, List[str]]
    match_score: float
    resume_keywords: List[str]
    jd_keywords: List[str]
    missing_keywords: List[str]
    resume_text: str
    job_profile_analysis: Optional[JobProfileScore] = None

class HealthCheck(BaseModel):
    status: str
    models_loaded: bool
    message: str
