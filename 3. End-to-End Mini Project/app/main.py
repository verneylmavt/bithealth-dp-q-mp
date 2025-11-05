# app/main.py for FastAPI entry point

from fastapi import FastAPI
from app.models import PatientInput, RecommendationResponse
from app.llm_chain import get_recommendation

app = FastAPI(
    title="Hospital Triage System",
    version="0.1.0",
)

@app.post("/recommend", response_model=RecommendationResponse)
async def recommend_department(patient: PatientInput):
    """
    Accepts patient and returns the department.
    """
    dept = get_recommendation(
        gender=patient.gender,
        age=patient.age,
        symptoms=patient.symptoms,
    )
    return RecommendationResponse(recommended_department=dept)
