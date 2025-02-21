import PyPDF2
import docx
from typing import Union

def parse_resume(file) -> str:
    """Parse a resume file (PDF or DOCX) and return the extracted text."""
    if file.filename.endswith('.pdf'):
        return parse_pdf(file)
    elif file.filename.endswith('.docx'):
        return parse_docx(file)
    else:
        raise ValueError("Unsupported file format. Please upload a PDF or DOCX file.")

def parse_pdf(file) -> str:
    """Extract text from a PDF file."""
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

def parse_docx(file) -> str:
    """Extract text from a DOCX file."""
    doc = docx.Document(file)
    text = ""
    for paragraph in doc.paragraphs:
        text += paragraph.text + "\n"
    return text