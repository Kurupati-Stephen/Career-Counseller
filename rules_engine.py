
def map_scores_to_careers(scores):
    """
    Maps user-assessed skill scores to potential career paths using rule-based logic.
    :param scores: dict with skill categories and score (1-5)
    :return: list of recommended careers
    """

    career_paths = []

    if scores.get("Tech Savvy", 0) >= 4 and scores.get("Logical Thinking", 0) >= 4:
        career_paths.append("Software Developer / AI Engineer")

    if scores.get("Creativity", 0) >= 4:
        career_paths.append("UI/UX Designer / Digital Artist")

    if scores.get("Empathy", 0) >= 4:
        career_paths.append("Psychologist / HR Manager")

    if scores.get("Leadership", 0) >= 4 and scores.get("Communication", 0) >= 3:
        career_paths.append("Entrepreneur / Project Manager")

    if scores.get("Logical Thinking", 0) >= 3 and scores.get("Communication", 0) >= 3:
        career_paths.append("Business Analyst / Consultant")

    if scores.get("Creativity", 0) >= 3 and scores.get("Empathy", 0) >= 3:
        career_paths.append("Marketing / Content Strategist")

    if not career_paths:
        career_paths.append("Generalist / Analyst roles")

    return career_paths
