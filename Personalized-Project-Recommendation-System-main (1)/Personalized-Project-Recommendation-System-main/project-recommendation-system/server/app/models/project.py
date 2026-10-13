from sqlalchemy import Column, Integer, String, Text
from app.database.base import Base


class Project(Base):

    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String(255), nullable=False)

    domain = Column(String(100))

    difficulty = Column(String(50))

    duration = Column(String(50))

    technologies = Column(Text)

    description = Column(Text)

    learning_outcomes = Column(Text)

    future_scope = Column(Text)

    project_type = Column(String(100))

    team_preference = Column(String(30))

    career_goal = Column(Text)

    interest_tags = Column(Text)

    prerequisites = Column(Text)

    estimated_complexity_score = Column(Integer)

    required_experience = Column(String(50))

    industry_domain = Column(Text)

    software_engineering_focus = Column(Text)

    embedding = Column(Text)