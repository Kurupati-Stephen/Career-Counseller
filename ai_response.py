# ai_response.py
import ollama

def get_ai_recommendation(name, interests, strengths, careers):
    prompt = f"""
    You are an expert career counsellor.
    Based on the following inputs:
    - Name: {name}
    - Interests: {interests}
    - Strengths: {strengths}
    - Career Paths: {', '.join(careers)}
    Provide a detailed and personalized career guidance summary in a friendly tone.
    """

    try:
        response = ollama.chat(
            model='llama3',
            messages=[{'role': 'user', 'content': prompt}]
        )
        # Extract the generated text
        return response['message']['content']

    except Exception as e:
        # Log or print the error if you want
        print(f"⚠️ Ollama error: {e}")
        # Return a safe fallback message
        return (
            "⚠️ Sorry, I couldn't generate a recommendation right now. "
            "Please try again in a moment."
        )
