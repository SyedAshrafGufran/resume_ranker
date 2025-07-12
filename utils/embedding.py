from sentence_transformers import SentenceTransformer

def load_model(model_name='all-MiniLM-L6-v2'):
    return SentenceTransformer(model_name)

def encode_texts(text_list, model):
    return model.encode(text_list, convert_to_tensor=True)