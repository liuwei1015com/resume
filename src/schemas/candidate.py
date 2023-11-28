from datetime import datetime
from typing import Optional

from .main import BaseModel, SuccessResponse


class CandidateInfoSchema(BaseModel):
    id: int
    name: str
    email: str
    phone: str
    address: str
    about: str


class CandidateSkillSchema(BaseModel):
    id: int
    name: str


class CandidateExperienceSchema(BaseModel):
    id: int
    company: str
    position: str
    description: str
    start_date: datetime
    end_date: Optional[datetime]


class CandidateEducationSchema(BaseModel):
    id: int
    school: str
    major: str
    description: str
    start_date: datetime
    end_date: Optional[datetime]


class CandidateData(BaseModel):
    info: CandidateInfoSchema
    skills: list[CandidateSkillSchema]
    experiences: list[CandidateExperienceSchema]
    educations: list[CandidateEducationSchema]


class CandidateResponse(SuccessResponse):
    data: CandidateData
