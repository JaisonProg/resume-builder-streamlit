import streamlit as st

st.title("Resume Builder (Streamlit Edition)")

# --- Input Fields ---
full_name = st.text_input("Full Name")
phone = st.text_input("Phone Number")
email = st.text_input("Email")
linkedin = st.text_input("LinkedIn URL")

summary = st.text_area("Professional Summary")
education = st.text_area("Education (one per line)")
experience = st.text_area("Work Experience (one per line)")
skills = st.text_input("Skills (comma-separated)")

# --- Button to Generate Resume ---
if st.button("Generate & Download Resume"):
    resume_text = f"{full_name.upper()}\n"
    resume_text += f"{phone} | {email} | {linkedin}\n\n"
    resume_text += "Professional Summary:\n" + summary + "\n\n"
    resume_text += "Education:\n" + "\n".join([f"- {e}" for e in education.splitlines() if e.strip()]) + "\n\n"
    resume_text += "Work Experience:\n" + "\n".join([f"- {w}" for w in experience.splitlines() if w.strip()]) + "\n\n"
    resume_text += "Skills:\n" + "\n".join([f"- {s.strip()}" for s in skills.split(",") if s.strip()])

    st.download_button(
        label="Download Your Resume",
        data=resume_text,
        file_name=f"{full_name.replace(' ', '_').lower()}_resume.txt",
        mime="text/plain"
    )