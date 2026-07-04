import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel("gemini-2.5-flash")


def ask_gemini(financial_summary, question):

    prompt = f"""
You are an expert personal finance advisor.

Analyze the user's financial information below.

{financial_summary}

User Question:
{question}

Give practical, concise financial advice.
"""

    response = model.generate_content(prompt)

    return response.text