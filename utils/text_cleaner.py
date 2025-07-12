import re
import spacy

# Load SpaCy English tokenizer, tagger, parser, NER, and word vectors
nlp = spacy.load("en_core_web_sm")

def clean_text(text):
    # Lowercase
    text = text.lower()

    # Remove email addresses
    text = re.sub(r'\S+@\S+', '', text)

    # Remove URLs
    text = re.sub(r'http\S+|www\S+|https\S+', '', text)

    # Remove special characters and numbers
    text = re.sub(r'[^a-zA-Z\s]', '', text)

    # Tokenize and remove stopwords and lemmatize
    doc = nlp(text)
    cleaned = ' '.join([token.lemma_ for token in doc if not token.is_stop and token.is_alpha])

    return cleaned
