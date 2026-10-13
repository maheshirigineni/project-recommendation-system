from fastapi import APIRouter
from app.services.llm_service import explain_projects

from app.schemas.recommendation import RecommendationRequest
from app.services.recommendation_service import get_recommendations

router = APIRouter()


@router.post("/recommend")
def recommend(request: RecommendationRequest):

    recommendations = get_recommendations(request.model_dump())

    response = []

    for item in recommendations:

        project = item["project"]
        response.append({
    "title": project.title,
    "domain": project.domain,
    "difficulty": project.difficulty,
    "duration": project.duration,
    "technologies": project.technologies,
    "description": project.description,
    "learning_outcomes": project.learning_outcomes,
    "future_scope": project.future_scope,

    "project_type": project.project_type,
    "team_preference": project.team_preference,
    "career_goal": project.career_goal,
    "interest_tags": project.interest_tags,
    "prerequisites": project.prerequisites,
    "estimated_complexity_score": project.estimated_complexity_score,
    "required_experience": project.required_experience,
    "industry_domain": project.industry_domain,
    "software_engineering_focus": project.software_engineering_focus,

    "similarity_score": round(item["score"], 4)
})
    
    llm_response = explain_projects(
    request.model_dump(),
    response
)

    return {
    "recommended_projects": response,
    "ai_explanation": llm_response
}
