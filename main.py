from ollama import chat

def get_user_input(prompt_text, is_rating=False):
    while True:
        user_input = input(prompt_text)
        if is_rating:
            if user_input.isdigit() and 1 <= int(user_input) <= 5:
                return int(user_input)
            else:
                print("❗ Invalid input. Enter a number from 1 to 5.")
        elif user_input.strip() != "":
            return user_input.strip()
        else:
            print("❗ Please enter a valid response.")

def main():
    print("🎓 Welcome to the AI Career Counsellor!\n")

    name = get_user_input("Enter your name: ")
    interests = get_user_input("What are your interests?: ")
    strengths = get_user_input("What do you think are your strengths?: ")

    print("\n🧠 Take this short quiz to evaluate your strengths (Rate 1–5):")
    logical = get_user_input("How confident are you solving logical problems? (1-5): ", is_rating=True)
    creative = get_user_input("Do you enjoy designing or creating things? (1-5): ", is_rating=True)
    empathy = get_user_input("Are you good at understanding others' feelings? (1-5): ", is_rating=True)
    leadership = get_user_input("Do you take initiative in group tasks? (1-5): ", is_rating=True)
    tech_comfort = get_user_input("How comfortable are you with technology? (1-5): ", is_rating=True)

    # Construct AI prompt
    prompt = f"""
You are a career guidance counselor.

Based on the following user profile, suggest 3 suitable career paths. Also provide a short reason for each suggestion and a learning path to get started.

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

        print("🎯 Career Suggestions:\n")
        print("DEBUG Raw Response:", response)

    except Exception as e:
        print("❌ An error occurred while generating AI response.")
        print(f"Error details: {e}")

if __name__ == "__main__":
    main()
