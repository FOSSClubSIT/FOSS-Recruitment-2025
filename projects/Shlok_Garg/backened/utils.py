from fastapi import HTTPException
from typing import List, Dict
import re
import io
import PyPDF2
from sklearn.metrics.pairwise import cosine_similarity

from ml_models import ner_pipeline, embedding_model, kw_model, spacy_nlp, job_model, resume_classifier
from job_profiles import JOB_PROFILES
from models import JobProfileScore

def extract_text_from_pdf(pdf_file) -> str:
    """Extract text from PDF file"""
    try:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text() + "\n"
        
        # Clean text
        text = re.sub(r'\s+', ' ', text)
        text = text.strip()
        return text
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error reading PDF: {str(e)}")

def extract_entities(text: str) -> Dict[str, List[str]]:
    """Extract named entities from text using enhanced NER pipeline with spaCy fallback"""
    result = {
        "names": [],
        "organizations": [],
        "skills": [],
        "locations": []
    }
    
    # Primary extraction using BERT NER
    if ner_pipeline:
        try:
            entities = ner_pipeline(text)
            
            for entity in entities:
                label = entity['entity_group']
                word = entity['word'].strip()
                confidence = entity.get('score', 1.0)
                
                # Only include high-confidence entities
                if confidence > 0.7:
                    if label in ['PER', 'PERSON'] and word not in result["names"]:
                        result["names"].append(word)
                    elif label in ['ORG', 'ORGANIZATION'] and word not in result["organizations"]:
                        result["organizations"].append(word)
                    elif label in ['LOC', 'LOCATION'] and word not in result["locations"]:
                        result["locations"].append(word)
        except Exception as e:
            print(f"Primary NER failed: {e}")
    
    # Fallback/Enhancement with spaCy
    if spacy_nlp:
        try:
            doc = spacy_nlp(text)
            for ent in doc.ents:
                if ent.label_ == "PERSON" and ent.text not in result["names"]:
                    result["names"].append(ent.text)
                elif ent.label_ == "ORG" and ent.text not in result["organizations"]:
                    result["organizations"].append(ent.text)
                elif ent.label_ in ["GPE", "LOC"] and ent.text not in result["locations"]:
                    result["locations"].append(ent.text)
        except Exception as e:
            print(f"spaCy NER failed: {e}")
    
    # Enhanced skills extraction with better patterns
    skill_patterns = [
        r'\b(?:Python|Java|JavaScript|TypeScript|React|Node\.js|Django|Flask|FastAPI|Spring Boot|Angular|Vue\.js|MongoDB|PostgreSQL|MySQL|Redis|Docker|Kubernetes|AWS|Azure|GCP|Git|HTML5?|CSS3?|SASS|SCSS|Bootstrap|Tailwind|jQuery|Express\.js|Laravel|Ruby on Rails|PHP|C\+\+|C#|Go|Rust|Swift|Kotlin|Scala|R|MATLAB|TensorFlow|PyTorch|Scikit-learn|Pandas|NumPy|Matplotlib|Seaborn|Jupyter|Machine Learning|Deep Learning|AI|Data Science|SQL|NoSQL|GraphQL|REST|API|Microservices|DevOps|CI/CD|Jenkins|GitLab|Linux|Unix|Windows|MacOS|Bash|Shell|PowerShell|Terraform|Ansible|Prometheus|Grafana|ELK|Elasticsearch|Logstash|Kibana|Apache Kafka|RabbitMQ|Nginx|Apache|Tomcat|Load Balancing|Hadoop|Spark|Airflow|Tableau|Power BI|Excel|Selenium|Jest|Cypress|Playwright|JUnit|TestNG|Figma|Adobe XD|Sketch|Photoshop|Illustrator|InDesign|Salesforce|HubSpot|Jira|Confluence|Slack|Microsoft Office|Google Workspace)\b'
    ]
    
    skills = []
    for pattern in skill_patterns:
        matches = re.findall(pattern, text, re.IGNORECASE)
        for match in matches:
            if match.lower() not in [s.lower() for s in skills]:
                skills.append(match)
    
    # Additional pattern-based skill extraction
    additional_patterns = [
        r'\b(?:Machine Learning|Artificial Intelligence|Data Analysis|Web Development|Mobile Development|Cloud Computing|Database Design|System Administration|Project Management|Agile|Scrum|Kanban|Test Automation|Quality Assurance|User Experience|User Interface|Digital Marketing|SEO|SEM|Social Media Marketing|Content Marketing|Email Marketing|Business Analysis|Financial Analysis|Risk Management|Compliance|Audit|Leadership|Team Management|Strategic Planning|Process Improvement|Change Management)\b'
    ]
    
    for pattern in additional_patterns:
        matches = re.findall(pattern, text, re.IGNORECASE)
        for match in matches:
            if match.lower() not in [s.lower() for s in skills]:
                skills.append(match)
    
    result["skills"] = skills[:25]  # Increased limit for better coverage
    
    return result

def extract_keywords(text: str, top_k: int = 20) -> List[str]:
    """Extract keywords using enhanced KeyBERT with better parameters"""
    if not kw_model:
        # Enhanced fallback to word frequency with better filtering
        words = re.findall(r'\b[a-zA-Z]{3,}\b', text.lower())
        word_freq = {}
        for word in words:
            word_freq[word] = word_freq.get(word, 0) + 1
        
        # Extended common words filter
        common_words = {
            'the', 'and', 'for', 'are', 'but', 'not', 'you', 'all', 'can', 'had', 'her', 'was', 'one', 'our', 'out', 
            'day', 'get', 'has', 'him', 'his', 'how', 'its', 'may', 'new', 'now', 'old', 'see', 'two', 'who', 'boy', 
            'did', 'man', 'way', 'end', 'why', 'let', 'put', 'say', 'she', 'too', 'use', 'will', 'work', 'years', 
            'experience', 'including', 'using', 'within', 'through', 'during', 'across', 'various', 'multiple'
        }
        
        # Filter technical and business relevant words
        tech_business_keywords = {
            'development', 'management', 'analysis', 'design', 'implementation', 'optimization', 'integration', 
            'architecture', 'framework', 'database', 'application', 'system', 'platform', 'solution', 'technology',
            'methodology', 'process', 'strategy', 'planning', 'execution', 'delivery', 'performance', 'quality'
        }
        
        filtered_words = {}
        for word, freq in word_freq.items():
            if (word not in common_words and len(word) > 3 and 
                (word in tech_business_keywords or freq >= 2)):
                filtered_words[word] = freq
        
        sorted_words = sorted(filtered_words.items(), key=lambda x: x[1], reverse=True)
        return [word for word, freq in sorted_words[:top_k]]
    
    try:
        # Enhanced KeyBERT parameters for better keyword extraction
        keywords = kw_model.extract_keywords(
            text, 
            keyphrase_ngram_range=(1, 3),  # Include up to 3-word phrases
            stop_words='english',
            use_maxsum=True,  # Use MaxSum for diversity
            nr_candidates=50,  # More candidates for better selection
            top_k=top_k,
            diversity=0.7  # Balance between relevance and diversity
        )
        return [kw[0] for kw in keywords]
    except Exception as e:
        print(f"Error in keyword extraction: {e}")
        return []

def calculate_match_score(resume_text: str, jd_text: str) -> float:
    """Calculate similarity score using enhanced embedding models"""
    if not jd_text:
        return 0.0
    
    try:
        # Use job-specific model if available, otherwise use main embedding model
        model_to_use = job_model if job_model else embedding_model
        
        if not model_to_use:
            return 0.0
        
        # Generate embeddings using the better model
        resume_embedding = model_to_use.encode([resume_text])
        jd_embedding = model_to_use.encode([jd_text])
        
        # Calculate cosine similarity
        similarity = cosine_similarity(resume_embedding, jd_embedding)[0][0]
        
        # Enhanced scoring with keyword overlap bonus
        resume_keywords = set(extract_keywords(resume_text, top_k=30))
        jd_keywords = set(extract_keywords(jd_text, top_k=30))
        
        # Calculate keyword overlap
        common_keywords = resume_keywords.intersection(jd_keywords)
        keyword_overlap_ratio = len(common_keywords) / max(len(jd_keywords), 1) if jd_keywords else 0
        
        # Combine semantic similarity with keyword overlap (weighted)
        final_score = (similarity * 0.7) + (keyword_overlap_ratio * 0.3)
        
        # Convert to percentage
        return round(float(final_score * 100), 2)
        
    except Exception as e:
        print(f"Error calculating match score: {e}")
        return 0.0

def detect_job_role(resume_text: str, entities: Dict[str, List[str]]) -> tuple[str, float]:
    """Detect the most likely job role from resume content"""
    text_lower = resume_text.lower()
    skills = [skill.lower() for skill in entities.get('skills', [])]
    
    role_scores = {}
    
    for role_id, profile in JOB_PROFILES.items():
        score = 0
        total_possible = 0
        
        # Check required skills
        required_found = 0
        for skill in profile['required_skills']:
            total_possible += 2  # Higher weight for required skills
            if any(skill.lower() in text_lower or skill.lower() in skills for skill in [skill]):
                required_found += 2
        
        # Check preferred skills  
        preferred_found = 0
        for skill in profile['preferred_skills']:
            total_possible += 1
            if any(skill.lower() in text_lower or skill.lower() in skills for skill in [skill]):
                preferred_found += 1
        
        # Check experience keywords
        experience_found = 0
        for keyword in profile['experience_keywords']:
            total_possible += 1
            if keyword.lower() in text_lower:
                experience_found += 1
        
        score = required_found + preferred_found + experience_found
        role_scores[role_id] = score / total_possible if total_possible > 0 else 0
    
    # Get the role with highest score
    if role_scores:
        best_role = max(role_scores.items(), key=lambda x: x[1])
        return best_role[0], best_role[1]
    
    return "software_engineer", 0.3  # Default fallback

def calculate_job_profile_score(resume_text: str, entities: Dict[str, List[str]], 
                               resume_keywords: List[str]) -> JobProfileScore:
    """Calculate comprehensive score against detected job profile"""
    
    # Detect job role
    detected_role, role_confidence = detect_job_role(resume_text, entities)
    profile = JOB_PROFILES[detected_role]
    
    text_lower = resume_text.lower()
    skills = [skill.lower() for skill in entities.get('skills', [])]
    
    category_scores = {}
    recommendations = []
    
    # Technical Skills Analysis
    tech_skills_found = []
    tech_skills_missing = []
    
    for skill in profile['required_skills']:
        if any(skill.lower() in text_lower or skill.lower() in skills for s in [skill]):
            tech_skills_found.append(skill)
        else:
            tech_skills_missing.append(skill)
    
    tech_score = len(tech_skills_found) / len(profile['required_skills']) * 100
    
    category_scores['technical_skills'] = {
        'score': tech_score,
        'found': tech_skills_found,
        'missing': tech_skills_missing[:5],  # Limit recommendations
        'weight': profile['weight_distribution'].get('technical_skills', 0.3)
    }
    
    if tech_score < 70:
        recommendations.extend([f"Add {skill} to strengthen technical profile" 
                              for skill in tech_skills_missing[:3]])
    
    # Tools & Frameworks Analysis
    tools_found = []
    tools_missing = []
    
    all_tools = profile['preferred_skills'] + profile.get('tools', [])
    for tool in all_tools:
        if any(tool.lower() in text_lower or tool.lower() in skills for t in [tool]):
            tools_found.append(tool)
        else:
            tools_missing.append(tool)
    
    tools_score = len(tools_found) / len(all_tools) * 100 if all_tools else 0
    
    framework_key = 'ml_tools' if detected_role == 'data_scientist' else 'frameworks'
    category_scores[framework_key] = {
        'score': tools_score,
        'found': tools_found,
        'missing': tools_missing[:5],
        'weight': profile['weight_distribution'].get(framework_key, 0.2)
    }
    
    if tools_score < 50:
        recommendations.extend([f"Consider learning {tool}" 
                              for tool in tools_missing[:2]])
    
    # Education Analysis
    education_keywords = profile['education']
    education_found = []
    
    for edu in education_keywords:
        if edu.lower() in text_lower:
            education_found.append(edu)
    
    education_score = min(len(education_found) / max(len(education_keywords) * 0.3, 1) * 100, 100)
    
    category_scores['education'] = {
        'score': education_score,
        'found': education_found,
        'missing': [],
        'weight': profile['weight_distribution'].get('education', 0.15)
    }
    
    if education_score < 30:
        recommendations.append("Consider highlighting relevant education or certifications")
    
    # Experience Analysis  
    experience_keywords = profile['experience_keywords']
    experience_found = []
    
    for exp in experience_keywords:
        if exp.lower() in text_lower:
            experience_found.append(exp)
    
    experience_score = len(experience_found) / len(experience_keywords) * 100
    
    category_scores['experience'] = {
        'score': experience_score,
        'found': experience_found,
        'missing': [exp for exp in experience_keywords if exp not in [e.lower() for e in experience_found]][:3],
        'weight': profile['weight_distribution'].get('experience', 0.15)
    }
    
    if experience_score < 60:
        recommendations.append("Add more specific project examples and achievements")
    
    # Soft Skills (basic check for leadership, communication, etc.)
    soft_skills_keywords = ["leadership", "communication", "team", "collaboration", "problem solving", "analytical"]
    soft_skills_found = []
    
    for skill in soft_skills_keywords:
        if skill.lower() in text_lower:
            soft_skills_found.append(skill)
    
    soft_skills_score = min(len(soft_skills_found) / max(len(soft_skills_keywords) * 0.4, 1) * 100, 100)
    
    category_scores['soft_skills'] = {
        'score': soft_skills_score,
        'found': soft_skills_found,
        'missing': [],
        'weight': profile['weight_distribution'].get('soft_skills', 0.1)
    }
    
    if soft_skills_score < 40:
        recommendations.append("Highlight leadership and communication skills")
    
    # Calculate overall weighted score
    overall_score = 0
    for category, data in category_scores.items():
        overall_score += data['score'] * data['weight']
    
    # Ensure we don't have too many recommendations
    recommendations = recommendations[:5]
    
    return JobProfileScore(
        detected_role=profile['title'],
        role_confidence=role_confidence,
        overall_score=round(overall_score, 1),
        category_scores=category_scores,
        recommendations=recommendations
    )

def find_missing_keywords(resume_keywords: List[str], jd_keywords: List[str]) -> List[str]:
    """Find keywords present in JD but missing in resume"""
    resume_lower = [kw.lower() for kw in resume_keywords]
    missing = []
    
    for jd_kw in jd_keywords:
        if jd_kw.lower() not in resume_lower:
            missing.append(jd_kw)
    
    return missing
