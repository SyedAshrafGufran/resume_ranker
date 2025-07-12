import streamlit as st
import os

from utils.resume_loader import load_resume_text
from utils.text_cleaner import clean_text
from utils.embedding import encode_texts as get_sentence_embeddings

from utils.ranker import rank_resumes

st.set_page_config(page_title="Smart Resume Ranker", layout="wide")

st.title("🤖 Smart Resume Ranker")
st.markdown("Rank resumes based on a selected or uploaded job description using NLP & sentence embeddings.")

# ---------------------------
# Load Job Description
# ---------------------------

st.sidebar.header("📄 Job Description Input")

# Choose from existing job descriptions
jd_files = [f for f in os.listdir("data") if f.endswith(".txt")]
jd_choice = st.sidebar.selectbox("Choose a Job Role", jd_files)

# Optionally upload custom job description
uploaded_jd = st.sidebar.file_uploader("Or Upload a Job Description", type=["txt"])

# Load and clean job description
if uploaded_jd is not None:
    job_description = uploaded_jd.read().decode("utf-8")
else:
    with open(os.path.join("data", jd_choice), "r", encoding="utf-8") as f:
        job_description = f.read()

st.subheader("📋 Job Description")
st.text_area("Edit if needed", value=job_description, height=250)

# ---------------------------
# Load Resumes
# ---------------------------

st.sidebar.header("📁 Resumes")
resume_dir = "resumes/sample_resumes"
uploaded_files = st.sidebar.file_uploader("Upload resumes", type=["pdf", "docx"], accept_multiple_files=True)

resumes = {}

if uploaded_files:
    for file in uploaded_files:
        try:
            resumes[file.name] = load_resume_text(file)
        except ValueError as e:
            st.warning(f"⚠️ {file.name}: {e}")

if st.button("🔍 Rank Resumes"):
    if not resumes:
        st.warning("⚠️ No resumes uploaded. Please upload at least one resume.")
    else:
        st.subheader("🏁 Ranking Resumes")
        jd_clean = clean_text(job_description)
        resume_texts = [clean_text(text) for _, text in resumes]

        embeddings = get_sentence_embeddings([jd_clean] + resume_texts)
        jd_vector = embeddings[0]
        resume_vectors = embeddings[1:]

        ranked_resumes = rank_resumes(resumes, jd_vector, resume_vectors)

        for idx, (filename, score) in enumerate(ranked_resumes, 1):
            st.markdown(f"### {idx}. 📄 {filename}")
            st.write(f"Similarity Score: **{score:.2f}**")
            st.progress(min(score, 1.0))  # keep bar within bounds

        st.success("✅ Ranking complete!")