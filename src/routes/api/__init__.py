from fastapi import APIRouter, Depends

from src.controllers import CandidateController
from src.crud import CandidateEducationCRUD, CandidateExperienceCRUD, CandidateInfoCRUD, CandidateSkillCRUD
from src.exceptions import JSendException
from src.schemas import CandidateData, CandidateResponse
from src.utils.connector import Session, get_db

api_router = APIRouter()


@api_router.get(
    "/candidates/{name}",
    summary="取得應徵者資訊",
    response_model=CandidateResponse,
)
def get_candidate(
    name: str,
    db: Session = Depends(get_db),
):
    stored_info = CandidateInfoCRUD.read_candidate_info_by_name(name, db)

    if not stored_info:
        return JSendException(404, "Candidate not found")

    candidate_id = stored_info.id

    stored_skills = CandidateSkillCRUD.read_candidate_skills_by_candidate_id(candidate_id, db)
    stored_experiences = CandidateExperienceCRUD.read_candidate_experiences_by_candidate_id(candidate_id, db)
    stored_educations = CandidateEducationCRUD.read_candidate_educations_by_candidate_id(candidate_id, db)

    info = CandidateController.wrap_candidate_info(stored_info)
    skills = []
    for stored_skill in stored_skills:
        skills.append(CandidateController.wrap_candidate_skill(stored_skill))
    experiences = []
    for stored_experience in stored_experiences:
        experiences.append(CandidateController.wrap_candidate_experience(stored_experience))
    educations = []
    for stored_education in stored_educations:
        educations.append(CandidateController.wrap_candidate_education(stored_education))

    data = CandidateData(
        info=info,
        skills=skills,
        experiences=experiences,
        educations=educations,
    )

    return CandidateResponse(data=data)
