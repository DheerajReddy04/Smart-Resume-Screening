import PyPDF2
import docx

def parse_resume(file):
    if file.filename.endswith('.pdf'):
        return parse_pdf(file)
    elif file.filename.endswith('.docx'):
        return parse_docx(file)
    else:
        return ""

def parse_pdf(file):
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def parse_docx(file):
    doc = docx.Document(file)
    text = ""
    for paragraph in doc.paragraphs:
        text += paragraph.text + "\n"
    return text
