from textblob import TextBlob

def analyze_sentiment(text: str) -> float:
    """Analyze sentiment of resume text."""
    blob = TextBlob(text)
    return blob.sentiment.polarity  # Returns a value between -1.0 (negative) and 1.0 (positive)