from typing import Dict, List

def generate_feedback(matched_skills: List[str], missing_skills: List[str], 
                     matched_experience: Dict[str, int], missing_experience: Dict[str, Dict[str, int]],
                     sentiment_score: float) -> str:
    """Generate personalized feedback for the candidate."""
    feedback = []

    # Feedback on skills
    if matched_skills:
        feedback.append(f"Great job highlighting your skills in: {', '.join(matched_skills)}.")
    if missing_skills:
        feedback.append(f"Consider adding experience or skills in: {', '.join(missing_skills)}.")

    # Feedback on experience
    if matched_experience:
        feedback.append(f"Your experience in {', '.join(matched_experience.keys())} is impressive.")
    if missing_experience:
        for title, details in missing_experience.items():
            feedback.append(
                f"For the role of {title}, you need {details['required']} months of experience "
                f"(you have {details['actual']} months)."
            )

    # Feedback on sentiment
    if sentiment_score > 0.5:
        feedback.append("Your resume has a very positive tone. Keep it up!")
    elif sentiment_score < -0.5:
        feedback.append("Your resume has a negative tone. Consider using more positive language.")
    else:
        feedback.append("Your resume has a neutral tone. Adding more positive language could help.")

    return " ".join(feedback)