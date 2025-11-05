# app/llm_chain.py for LangChain code that talks to the LLM

import os
from typing import List, Optional
from dotenv import load_dotenv
from pathlib import Path

from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI


# Simple rule-based fallback
def simple_rule_based_classifier(symptoms: List[str]) -> str:
    """
    Small heuristic, if LLM is not available.
    """
    text = " ".join(s.lower() for s in symptoms)
    if any(k in text for k in ["pusing", "kehilangan keseimbangan", "sulit berjalan", "kejang"]):
        return "Neurology"
    if any(k in text for k in ["sesak", "sesak napas", "sesak nafas", "batuk", "menggigil"]):
        return "Pulmonology"
    if any(k in text for k in ["nyeri dada", "jantung", "berdebar"]):
        return "Cardiology"
    if any(k in text for k in ["sakit perut", "mual", "muntah"]):
        return "Gastroenterology"
    return "General Medicine"


# LLM interaction function
def build_prompt(gender: str, age: int, symptoms: List[str]) -> str:
    symptoms_text = ", ".join(symptoms)
    prompt = f"""
You are a clinical triage assistant in an Indonesian hospital.
Your job is to read patient demographic info and free-text symptoms
and suggest the single most relevant specialist department
for the first referral.

Respond with ONLY the department name in Indonesian/English medical context,
for example: "Neurology", "Cardiology", "Pulmonology", "Orthopedics",
"Gastroenterology", "Dermatology", "Psychiatry", "Obstetrics/Gynecology".

Patient info:
- Gender: {gender}
- Age: {age}
- Symptoms: {symptoms_text}

Department (one word only):
""".strip()
    return prompt



def get_recommendation(gender: str, age: int, symptoms: List[str]) -> str:
    """
    Main function of FastAPI handler.
    Try LLM first. If error, falls to rule-based.
    """
    load_dotenv(Path("..") / ".env")
    api_key = os.getenv("GOOGLE_API_KEY")
    prompt = build_prompt(gender, age, symptoms)

    if not api_key:
        # LLM not configured, use fallback
        return simple_rule_based_classifier(symptoms)

    try:
        llm = ChatGoogleGenerativeAI(
            model="gemini-1.5-flash",
            google_api_key=api_key, 
            temperature=0.2,
        )

        # Send prompt as human message
        response = llm.invoke([HumanMessage(content=prompt)])

        # response.content contain department name
        dept = response.content.strip()

        # Harden output (if LLM gives a sentence, take first token/line)
        if "\n" in dept:
            dept = dept.split("\n")[0].strip()
        return dept
    except Exception:
        # If LLM call fails, use fallback
        return simple_rule_based_classifier(symptoms)