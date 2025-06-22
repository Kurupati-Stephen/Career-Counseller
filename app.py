import streamlit as st
from ai_response import get_ai_recommendation
from chart import plot_scores
from fpdf import FPDF
from action_plan import get_action_plan
from email.message import EmailMessage
from deep_translator import GoogleTranslator
import smtplib

# --- Page Config & Logo ---
st.set_page_config(page_title="AI Career Counsellor", page_icon="🎓")
st.image("https://i.imgur.com/9XnL5nH.png", width=100)
st.title("🎓 AI Career Counsellor")
st.markdown("Empowering your future, one suggestion at a time!")

# --- Assessment Section ---
with st.expander("📝 Take a quick assessment (optional but improves accuracy)"):
    tech = st.slider("Your interest in technology?", 1, 5, 3)
    comm = st.slider("Your communication skills?", 1, 5, 3)
    lead = st.slider("How well do you handle leadership tasks?", 1, 5, 3)
    create = st.slider("Your creativity level?", 1, 5, 3)
    logic = st.slider("How logical are you in solving problems?", 1, 5, 3)
    scores = {
        "Tech": tech,
        "Communication": comm,
        "Leadership": lead,
        "Creativity": create,
        "Logic": logic
    }

# --- Input Section ---
user_input = st.text_area("💬 Ask your career question:")
email = st.text_input("📧 Enter your email (optional, for sending result):")

# --- Language Selection ---
lang_choice = st.selectbox("🌍 Choose a language:", ["English", "Telugu", "Hindi"])

# --- Button Click Action ---
if st.button("Get Advice"):
    if not user_input.strip():
        st.warning("Please enter your question.")
    else:
        with st.spinner("AI is thinking..."):
            ai_response, career_name = get_ai_recommendation(user_input, scores)

            # Translate if needed
            if lang_choice != "English":
                lang_code = "te" if lang_choice == "Telugu" else "hi"
                ai_response = GoogleTranslator(source="auto", target=lang_code).translate(ai_response)

            # Display response
            st.success("🧠 Recommendation:")
            st.markdown(ai_response)

            # --- Chart Display ---
            st.pyplot(plot_scores(scores))

            # --- Action Plan ---
            st.subheader("📌 Your Action Plan:")
            try:
                plan = get_action_plan(career_name)
            except Exception:
                plan = get_action_plan("General")

            for step in plan:
                st.checkbox(step)

            # --- PDF DOWNLOAD ---
            if st.button("📄 Download as PDF"):
                pdf = FPDF()
                pdf.add_page()
                pdf.set_font("Arial", size=12)
                pdf.multi_cell(0, 10, f"AI Career Counsellor Recommendation:\n\n{ai_response}\n\nScores: {scores}\n")
                pdf.output("career_recommendation.pdf")
                with open("career_recommendation.pdf", "rb") as file:
                    st.download_button("📅 Download PDF", file, "Career_Advice.pdf")

            # --- EMAIL FEATURE ---
            if email:
                try:
                    msg = EmailMessage()
                    msg['Subject'] = "Your Career Counsellor Advice"
                    msg['From'] = st.secrets["EMAIL"]
                    msg['To'] = email
                    msg.set_content(f"Here is your AI Career Counsellor recommendation:\n\n{ai_response}")

                    server = smtplib.SMTP("smtp.gmail.com", 587)
                    server.starttls()
                    server.login(st.secrets["EMAIL"], st.secrets["EMAIL_PASSWORD"])
                    server.send_message(msg)
                    server.quit()
                    st.success("📬 Recommendation sent to your email!")
                except Exception as e:
                    st.error(f"Failed to send email: {e}")

            # --- Gamification Badge ---
            if all(v >= 4 for v in scores.values()):
                st.balloons()
                st.success("🌼 Badge Unlocked: Multi-Talent Explorer!")

            # --- Chat Log ---
            if "history" not in st.session_state:
                st.session_state.history = []
            st.session_state.history.append({"q": user_input, "a": ai_response})

            st.subheader("📜 Conversation History")
            for item in st.session_state.history:
                st.markdown(f"**Q:** {item['q']}  \n**A:** {item['a']}")
