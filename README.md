# 🤖 Smart Resume Ranker

**Smart Resume Ranker** is an NLP-powered web app that ranks resumes based on how well they match a given job description. It uses sentence embeddings to semantically compare resumes and job descriptions, helping recruiters or job seekers identify the best fit quickly.

---

## 🔍 Features

- Upload a job description or choose from predefined ones
- Upload multiple resumes (PDF or DOCX)
- Ranks resumes based on semantic similarity
- Displays similarity scores and progress bars
- Fully interactive UI built with Streamlit

---

## 🛠 Tech Stack

- **Python 3.8+**
- **Streamlit** – Web UI
- **Sentence Transformers** – Embeddings
- **PDFPlumber** – PDF resume text extraction
- **python-docx** – DOCX resume handling
- **scikit-learn** – Cosine similarity
- **NLP tools** – Text preprocessing & normalization