def map_scores_to_careers(scores):
    career_paths = []

    if scores["Tech Savvy"] >= 4 and scores["Logical Thinking"] >= 4:
        career_paths.append("Software Developer / AI Engineer")
    if scores["Creativity"] >= 4:
        career_paths.append("UI/UX Designer / Digital Artist")
    if scores["Empathy"] >= 4:
        career_paths.append("Psychologist / HR Manager")
    if scores["Leadership"] >= 4:
        career_paths.append("Entrepreneur / Project Manager")

    if not career_paths:
        career_paths.append("Generalist / Analyst roles")

    return career_paths
