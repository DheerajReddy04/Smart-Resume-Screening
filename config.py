import os

class Config:
    # Secret key for session management
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_secret_key_here'

    # Upload folder for resumes
    UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)

    # Allowed file extensions
    ALLOWED_EXTENSIONS = {'pdf', 'docx'}

    # spaCy model path
    SPACY_MODEL = 'en_core_web_sm'

    # Paths to model files
    SKILLS_DATABASE_PATH = os.path.join(os.getcwd(), 'models', 'skills_database.json')
    FRAUD_PATTERNS_PATH = os.path.join(os.getcwd(), 'models', 'fraud_patterns.json')
    FEEDBACK_TEMPLATES_PATH = os.path.join(os.getcwd(), 'models', 'feedback_templates.json')