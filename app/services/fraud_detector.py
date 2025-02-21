import re
import json
from typing import Dict, List

# Load fraud patterns
with open('models/fraud_patterns.json') as f:
    FRAUD_PATTERNS = json.load(f)

def detect_fraud(text: str) -> Dict[str, List[str]]:
    """Detect fraudulent content in resume text."""
    report = {'fake_universities': [], 'suspicious_phrases': []}

    # Check for fake universities
    for uni in FRAUD_PATTERNS['fake_universities']:
        if re.search(uni.lower(), text.lower()):
            report['fake_universities'].append(uni)

    # Check for suspicious phrases
    for phrase in FRAUD_PATTERNS['suspicious_phrases']:
        if re.search(phrase.lower(), text.lower()):
            report['suspicious_phrases'].append(phrase)

    return report