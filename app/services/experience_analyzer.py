import re
from typing import Dict, List

def extract_experience(text: str) -> Dict[str, int]:
    """
    Extract work experience from resume text.
    Returns a dictionary with job titles and their durations in months.
    """
    experience = {}
    # Regex to find job titles and durations
    pattern = r"(?i)(\b\w+\b.*?)\s*\((\d+\+?)\s*(years?|months?)\)"
    matches = re.findall(pattern, text)

    for title, duration, unit in matches:
        duration = int(duration)
        if "year" in unit.lower():
            duration *= 12  # Convert years to months
        experience[title.strip()] = duration

    return experience

def match_experience(resume_experience: Dict[str, int], job_requirements: Dict[str, int]) -> Dict[str, Dict[str, int]]:
    """
    Match resume experience with job requirements.
    Returns a dictionary with matched and missing experience.
    """
    matched_experience = {}
    missing_experience = {}

    for title, required_duration in job_requirements.items():
        if title in resume_experience:
            if resume_experience[title] >= required_duration:
                matched_experience[title] = resume_experience[title]
            else:
                missing_experience[title] = {
                    "required": required_duration,
                    "actual": resume_experience[title]
                }
        else:
            missing_experience[title] = {
                "required": required_duration,
                "actual": 0
            }

    return {
        "matched_experience": matched_experience,
        "missing_experience": missing_experience
    }