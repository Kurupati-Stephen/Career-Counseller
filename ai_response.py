from ollama import chat

def get_ai_recommendation(question, scores):
    # Dynamically create the profile string from the scores dictionary
    profile = "User profile:\n"
    for trait, value in scores.items():
        profile += f"- {trait}: {value}/5\n"

    # Construct the AI prompt
    prompt = f"""
You are a professional career counsellor.

Based on this user profile and question, suggest 3 suitable career paths.
Give a short reason for each and clearly mention one recommended career at the end.

{profile}

User Question: {question}
"""

    # Call the Ollama LLaMA 3 model
    response = chat(model='llama3', messages=[
        {"role": "system", "content": "You are a helpful AI career advisor."},
        {"role": "user", "content": prompt}
    ])

    reply = response["message"]["content"]

    # Extract the recommended career if mentioned explicitly
    recommended = "General"
    for line in reply.splitlines():
        if "recommended" in line.lower():
            recommended = line.split(":")[-1].strip()
            break

    return reply, recommended
