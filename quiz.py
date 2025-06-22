import streamlit as st

def run_quiz():
    """
    Streamlit-based personality and skills quiz (1–5 scale).
    Returns a dictionary of scores.
    """
    st.subheader("📝 Take the Career Strengths Quiz")
    st.markdown("Rate yourself on each of the following (1 = Low, 5 = High)")

    logical = st.slider("Logical Thinking: How confident are you solving logical problems?", 1, 5, 3)
    creative = st.slider("Creativity: Do you enjoy designing or creating things?", 1, 5, 3)
    empathy = st.slider("Empathy: Are you good at understanding others' feelings?", 1, 5, 3)
    leader = st.slider("Leadership: Do you take initiative in group tasks?", 1, 5, 3)
    tech = st.slider("Tech Savvy: How comfortable are you with technology?", 1, 5, 3)

    scores = {
        "Logical Thinking": logical,
        "Creativity": creative,
        "Empathy": empathy,
        "Leadership": leader,
        "Tech Savvy": tech
    }

    return scores