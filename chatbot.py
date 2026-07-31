import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def ask_ai(question, company_data):

    prompt = f"""
You are an Employee Support AI Assistant for TechNova Solutions Pvt. Ltd.

Answer ONLY using the company information provided below.

If the answer is not available, reply:

"I couldn't find that information in the company knowledge base."

Company Information:

{company_data}

Employee Question:

{question}

Answer:
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2,
        max_tokens=500
    )

    return response.choices[0].message.content

def generate_email(email_type, employee, recipient, purpose):

    prompt = f"""
You are a professional business email assistant.

Write a formal email.

Email Type: {email_type}

Employee Name: {employee}

Recipient: {recipient}

Purpose:
{purpose}

Generate:

Subject:

Email:
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3,
        max_tokens=500
    )

    return response.choices[0].message.content