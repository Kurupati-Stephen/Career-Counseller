def run_quiz():
    print("\n🧠 Take this short quiz to evaluate your strengths (Rate 1–5):")
    questions = {
        "Logical Thinking": "How confident are you solving logical problems?",
        "Creativity": "Do you enjoy designing or creating things?",
        "Empathy": "Are you good at understanding others' feelings?",
        "Leadership": "Do you take initiative in group tasks?",
        "Tech Savvy": "How comfortable are you with technology?",
    }

    scores = {}
    for trait, question in questions.items():
        while True:
            try:
                score = int(input(f"{question} (1-5): "))
                if 1 <= score <= 5:
                    scores[trait] = score
                    break
                else:
                    print("❗ Please enter a value between 1 and 5.")
            except:
                print("❗ Invalid input. Enter a number.")
    return scores
