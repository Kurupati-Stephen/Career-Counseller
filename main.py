from ollama import chat

def get_user_input(prompt_text, is_rating=False):
    while True:
        user_input = input(prompt_text)
        if is_rating:
            if user_input.isdigit() and 1 <= int(user_input) <= 5:
                return int(user_input)
            else:
                print("❗ Please enter a number from 1 to 5.")
        elif user_input.strip() != "":
            return user_input.strip()
        else:
            print("❗ Please enter a valid response.")

def main():
    print("🎓 Welcome to the AI Career Counsellor!\n")

    # Collect user information
    name = get_user_input("Enter your name: ")
    interests = get_user_input("What are your interests?: ")
    strengths = get_user_input("What do you think are your strengths?: ")

    # Career quiz
    print("\n🧠 Quick Strengths Quiz (Rate 1–5):")
    logical = get_user_input("Logical Thinking (1-5): ", is_rating=True)
    creative = get_user_input("Creativity (1-5): ", is_rating=True)
    empathy = get_user_input("Empathy (1-5): ", is_rating=True)
    leadership = get_user_input("Leadership (1-5): ", is_rating=True)
    tech_comfort = get_user_input("Tech Comfort (1-5): ", is_rating=True)

    # Construct prompt
    prompt = f"""
You are a professional career counselor.

Based on the user's profile below, suggest three suitable career options. Provide a short explanation for each and a beginner-friendly learning path.

User Profile:
- Name: {name}
- Interests: {interests}
- Strengths: {strengths}
- Logical Thinking: {logical}/5
- Creativity: {creative}/5
- Empathy: {empathy}/5
- Leadership: {leadership}/5
- Comfort with Technology: {tech_comfort}/5
"""

    print("\n🤖 Generating your personalized career advice...\n")

    try:
        response = chat(model='llama3', messages=[
            {"role": "system", "content": "You are a helpful AI career counsellor."},
            {"role": "user", "content": prompt}
        ])
        result = response["message"]["content"]
        print("🎯 Career Suggestions:\n")
        print(result)

    except Exception as e:
        print("❌ An error occurred while generating the response.")
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
