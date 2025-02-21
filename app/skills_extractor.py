import json
import spacy

# Load pre-defined skills from a JSON file
with open('models/job_skills.json') as f:
    JOB_SKILLS = json.load(f)

# Load spaCy model
nlp = spacy.load('en_core_web_sm')

def extract_skills(text):
    doc = nlp(text.lower())
    extracted_skills = set()
    for token in doc:
        if token.text in JOB_SKILLS:
            extracted_skills.add(token.text)
    return list(extracted_skills)
