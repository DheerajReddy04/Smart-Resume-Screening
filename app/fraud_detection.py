import re

def detect_fraud(text):
    fraud_indicators = {
        'fake_universities': ['University of Nowhere', 'Fake Institute of Technology'],
        'suspicious_phrases': ['guaranteed placement', 'buy degree']
    }
    report = {'fake_universities': [], 'suspicious_phrases': []}

    for uni in fraud_indicators['fake_universities']:
        if re.search(uni.lower(), text.lower()):
            report['fake_universities'].append(uni)

    for phrase in fraud_indicators['suspicious_phrases']:
        if re.search(phrase.lower(), text.lower()):
            report['suspicious_phrases'].append(phrase)

    return report
