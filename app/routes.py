from flask import Blueprint, render_template, request, redirect, url_for
from .resume_parser import parse_resume
from .skills_extractor import extract_skills
from .fraud_detection import detect_fraud
from .sentiment_analysis import analyze_sentiment

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/upload', methods=['POST'])
def upload_resume():
    if 'resume' not in request.files:
        return redirect(url_for('main.index'))

    resume_file = request.files['resume']
    if resume_file.filename == '':
        return redirect(url_for('main.index'))

    # Parse the resume
    resume_text = parse_resume(resume_file)

    # Extract skills
    skills = extract_skills(resume_text)

    # Detect fraud
    fraud_report = detect_fraud(resume_text)

    # Analyze sentiment
    sentiment_score = analyze_sentiment(resume_text)

    return render_template('result.html', skills=skills, fraud_report=fraud_report, sentiment_score=sentiment_score)
