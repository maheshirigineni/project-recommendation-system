from pydantic import BaseModel


class RecommendationRequest(BaseModel):
    domain: str
    difficulty: str
    duration: str
    technologies: str

    career_goal: str
    interests: str
    required_experience: str
    team_preference: str