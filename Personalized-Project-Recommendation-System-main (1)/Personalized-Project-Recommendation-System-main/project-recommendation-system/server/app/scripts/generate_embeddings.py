import json

from sentence_transformers import SentenceTransformer

from app.database.connection import SessionLocal
from app.models.project import Project

from app.services.embedding_service import generate_embedding
# Load embedding model
#model = SentenceTransformer("BAAI/bge-small-en-v1.5")

# Database session
db = SessionLocal()

# Fetch all projects
projects = db.query(Project).all()

print(f"Found {len(projects)} projects.")

for project in projects:

    text = f"""
    Title: {project.title}

    Domain: {project.domain}

    Difficulty: {project.difficulty}

    Duration: {project.duration}

    Technologies: {project.technologies}

    Description:
    {project.description}

    Learning Outcomes:
    {project.learning_outcomes}

    Future Scope:
    {project.future_scope}
    """

    # Generate embedding
    embedding = generate_embedding(text)

    # Store as JSON string
    project.embedding = json.dumps(embedding.tolist())

db.commit()
db.close()

print("Embeddings generated successfully!")