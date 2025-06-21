import streamlit as st
from ollama import chat  # Make sure ollama is installed and running

st.set_page_config(page_title="AI Career Counsellor", layout="centered")

st.title("🎯 AI Career Counsellor")
st.markdown("Answer a few questions and get personalized career guidance powered by AI!")

# --- Input Form ---
with st.form("career_form"):
    name = st.text_input("👤 Name")
    age = st.number_input("🎂 Age", min_value=10, max_value=100, step=1)
    qualification = st.selectbox("🎓 Highest Qualification", 
                                 ["High School", "Diploma", "Bachelor's", "Master's", "PhD"])
    field = st.selectbox("💼 Field of Interest", 
                         ["Software Development", "Data Science", "AI/ML", "Cybersecurity", 
                          "Networking", "Cloud Computing", "Digital Marketing", "Design", "Other"])
    experience = st.slider("📊 Years of Experience", 0, 20, 0)
    skills = st.text_area("🛠️ List Your Key Skills (comma-separated)")
    work_style = st.radio("🏢 Preferred Work Style", ["Remote", "On-site", "Hybrid"])
    goals = st.text_area("🎯 Career Goals")
    location = st.text_input("📍 Preferred Job Location (Optional)")

    st.markdown("### 🧠 Self-Evaluation (Rate Yourself 1–5):")
    logical = st.slider("🔢 Logical Thinking", 1, 5, 3)
    creative = st.slider("🎨 Creativity", 1, 5, 3)
    empathy = st.slider("🤝 Empathy", 1, 5, 3)
    leadership = st.slider("🗣️ Leadership", 1, 5, 3)
    tech_comfort = st.slider("💻 Comfort with Technology", 1, 5, 3)

    submitted = st.form_submit_button("🚀 Get Career Recommendations")

# --- On Submit ---
if submitted:
    if name.strip() == "" or goals.strip() == "":
        st.warning("⚠️ Please fill in all required fields.")
    else:
        # Combine user input into a prompt
        user_prompt = f"""
        I'm {name}, {age} years old, with a qualification of {qualification}. 
        I'm interested in {field}. I have {experience} years of experience. 
        My key skills include: {skills}. I prefer {work_style} work.
        My career goals are: {goals}.
        Preferred job location: {location if location else 'not specified'}.

        Here is my self-evaluation:
        - Logical Thinking: {logical}/5
        - Creativity: {creative}/5
        - Empathy: {empathy}/5
        - Leadership: {leadership}/5
        - Comfort with Technology: {tech_comfort}/5

        Based on this, suggest:
        1. Top 3 career roles
        2. Description of each role
        3. Skills/tools required
        4. Courses or certifications to take
        5. Any additional career tips.
        Format the response with bullet points and clear headings.
        """

        with st.spinner("⏳ AI is thinking... this may take a few seconds"):
            try:
                response = chat(model="llama3", messages=[{"role": "user", "content": user_prompt}])
                answer = response["message"]["content"]
                st.success("✅ Here are your personalized career recommendations:")
                st.markdown(answer)
            except Exception as e:
                st.error(f"❌ Error generating response: {e}")
