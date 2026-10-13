import os

from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)
def explain_projects(user, projects):

    prompt = f"""
You are an expert software mentor.

User Profile:
{user}

Recommended Projects:
{projects}

For each project explain:

1. Why it suits the user.
2. What skills the user will learn.
3. A roadmap to build the project.
4. Expected challenges.
5. Future improvements.

Return the answer in clean Markdown.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content