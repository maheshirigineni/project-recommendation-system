import pandas as pd

from app.database.connection import SessionLocal
from app.models.project import Project

db = SessionLocal()

df = pd.read_csv("software_projects_250.csv")

for _, row in df.iterrows():
    project = Project(

    title=row["title"],

    domain=row["domain"],

    difficulty=row["difficulty"],

    duration=row["duration"],

    technologies=row["technologies"],

    description=row["description"],

    learning_outcomes=row["learning_outcomes"],

    future_scope=row["future_scope"],

    project_type=row["project_type"],

    team_preference=row["team_preference"],

    career_goal=row["career_goal"],

    interest_tags=row["interest_tags"],

    prerequisites=row["prerequisites"],

    estimated_complexity_score=row["estimated_complexity_score"],

    required_experience=row["required_experience"],

    industry_domain=row["industry_domain"],

    software_engineering_focus=row["software_engineering_focus"]

)


    db.add(project)

db.commit()
db.close()

print("Projects imported successfully!")