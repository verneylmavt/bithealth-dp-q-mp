# app/models.py for Pydantic request/response models

from pydantic import BaseModel
from typing import List

class PatientInput(BaseModel):
    gender: str
    age: int
    symptoms: List[str]

class RecommendationResponse(BaseModel):
    recommended_department: str