from sentence_transformers import SentenceTransformer

# Load model only once when FastAPI starts
model = SentenceTransformer("BAAI/bge-small-en-v1.5")


def generate_embedding(text: str):
    """
    Converts any text into a semantic embedding.
    """
    return model.encode(text)