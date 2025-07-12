from sklearn.metrics.pairwise import cosine_similarity

def rank_resumes(jd_text, resume_texts, embed_fn):
    """
    Ranks resumes based on semantic similarity with the job description.

    Args:
        jd_text (str): The job description text.
        resume_texts (List[str]): List of resume texts.
        embed_fn (Callable): Function to convert texts into embeddings.

    Returns:
        List[Tuple[int, float]]: List of tuples (index, similarity_score), sorted by score.
    """
    all_texts = [jd_text] + resume_texts
    embeddings = embed_fn(all_texts)

    jd_vector = embeddings[0]
    resume_vectors = embeddings[1:]

    # Calculate cosine similarity
    similarities = cosine_similarity([jd_vector], resume_vectors)[0]

    # Return ranked list of (index, similarity) sorted descending
    ranked = sorted(enumerate(similarities), key=lambda x: x[1], reverse=True)
    return ranked
