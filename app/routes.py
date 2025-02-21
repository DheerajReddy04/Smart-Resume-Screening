from flask import Blueprint, render_template, request, redirect, url_for, flash
from .services.resume_parser import parse_resume
from .services.skills_matcher import extract_skills, match_skills
from .services.experience_analyzer import extract_experience, match_experience
from .services.fraud_detector import detect_fraud
from .services.sentiment_analyzer import analyze_sentiment
from .services.feedback_generator import generate_feedback
import os

main = Blueprint('main', __name__)

# Example job requirements
JOB_REQUIREMENTS = {
    "skills": ["Python", "Machine Learning", "Data Analysis"],
    "experience": {
        "Data Scientist": 24,  # 24 months of experience required
        "Software Engineer": 12
    }
}

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/upload', methods=['POST'])
def upload_resume():
    if 'resume' not in request.files:
        flash('No file uploaded.', 'error')
        return redirect(url_for('main.index'))

    resume_file = request.files['resume']
    if resume_file.filename == '':
        flash('No file selected.', 'error')
        return redirect(url_for('main.index'))

    try:
        # Parse the resume
        resume_text = parse_resume(resume_file)

        # Extract and match skills
        resume_skills = extract_skills(resume_text)
        skills_report = match_skills(resume_skills, JOB_REQUIREMENTS['skills'])

        # Extract and match experience
        resume_experience = extract_experience(resume_text)
        experience_report = match_experience(resume_experience, JOB_REQUIREMENTS['experience'])

        # Detect fraud
        fraud_report = detect_fraud(resume_text)

        # Analyze sentiment
        sentiment_score = analyze_sentiment(resume_text)

        # Generate feedback
        feedback = generate_feedback(skills_report['matched_skills'],skills_report['missing_skills'],experience_report['matched_experience'],experience_report['missing_experience'],sentiment_score)

        return render_template('analysis.html', 
                               skills=resume_skills,
                               skills_report=skills_report,
                               experience_report=experience_report,
                               fraud_report=fraud_report,
                               sentiment_score=sentiment_score,
                               feedback=feedback)
    except Exception as e:
        flash(f'An error occurred: {str(e)}', 'error')
        return redirect(url_for('main.index'))