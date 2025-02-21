import json
import spacy
from typing import List

# Load spaCy model
nlp = spacy.load('en_core_web_sm')

# Load skills database
with open('models/skills_database.json') as f:
    SKILLS_DATABASE = json.load(f)['skills']

def extract_skills(text: str) -> List[str]:
    """Extract skills from resume text using NLP."""
    doc = nlp(text.lower())
    extracted_skills = set()
    for token in doc:
        if token.text in SKILLS_DATABASE:
            extracted_skills.add(token.text)
    return list(extracted_skills)

def match_skills(resume_skills: List[str], job_skills: List[str]) -> dict:
    """Match resume skills with job requirements."""
    matched_skills = set(resume_skills).intersection(set(job_skills))
    missing_skills = set(job_skills).difference(set(resume_skills))
    return {
        'matched_skills': list(matched_skills),
        'missing_skills': list(missing_skills)
    }