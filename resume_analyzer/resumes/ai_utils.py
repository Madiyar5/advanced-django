def extract_skills(text):
    keywords = ["Python", "Django", "JavaScript", "SQL", "AWS", "React", "Docker"]
    found_skills = [word for word in keywords if word.lower() in text.lower()]
    return found_skills

def extract_experience(text):
    lines = text.split("\n")
    return [line for line in lines if "experience" in line.lower()]

def extract_education(text):
    lines = text.split("\n")
    return [line for line in lines if "university" in line.lower() or "bachelor" in line.lower()]