import json

from sklearn.metrics.pairwise import cosine_similarity

from app.database.connection import SessionLocal
from app.models.project import Project
from app.services.embedding_service import generate_embedding


def get_recommendations(user):

    db = SessionLocal()

    user_text = f"""
    Domain: {user["domain"]}
    Technologies: {user["technologies"]}
    Career Goal: {user["career_goal"]}
    Description: {user["interests"]}
    """

    user_embedding = generate_embedding(user_text)

    recommendations = []

    projects = db.query(Project).all()

    for project in projects:

        project_embedding = json.loads(project.embedding)

        semantic_score = cosine_similarity(
            [user_embedding],
            [project_embedding]
        )[0][0]

        structured_score = 0

        if user["domain"].lower() == project.domain.lower():
            structured_score += 0.15

        if user["duration"].lower() == project.duration.lower():
            structured_score += 0.03

        if user["required_experience"].lower() == project.required_experience.lower():
            structured_score += 0.04

        if user["team_preference"].lower() == project.team_preference.lower():
            structured_score += 0.01

        final_score = semantic_score * 0.60 + structured_score

        recommendations.append({
            "project": project,
            "score": final_score
        })

    db.close()

    recommendations.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return recommendations[:5]