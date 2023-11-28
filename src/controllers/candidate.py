from src.models import CandidateEducation, CandidateExperience, CandidateInfo, CandidateSkill
from src.schemas import CandidateEducationSchema, CandidateExperienceSchema, CandidateInfoSchema, CandidateSkillSchema


class CandidateController:
    @staticmethod
    def wrap_candidate_info(
        stored_candidate_info: CandidateInfo,
    ) -> CandidateInfoSchema:
        return CandidateInfoSchema(
            id=stored_candidate_info.id,
            name=stored_candidate_info.name,
            email=stored_candidate_info.email,
            phone=stored_candidate_info.phone,
            address=stored_candidate_info.address,
            about=stored_candidate_info.about,
        )

    @staticmethod
    def wrap_candidate_skill(
        stored_candidate_skill: CandidateSkill,
    ) -> CandidateSkillSchema:
        return CandidateSkillSchema(
            id=stored_candidate_skill.id,
            name=stored_candidate_skill.name,
        )

    @staticmethod
    def wrap_candidate_experience(
        stored_candidate_experience: CandidateExperience,
    ) -> CandidateExperienceSchema:
        return CandidateExperienceSchema(
            id=stored_candidate_experience.id,
            company=stored_candidate_experience.company,
            position=stored_candidate_experience.position,
            description=stored_candidate_experience.description,
            start_date=stored_candidate_experience.start_date,
            end_date=stored_candidate_experience.end_date,
        )

    @staticmethod
    def wrap_candidate_education(
        stored_candidate_education: CandidateEducation,
    ) -> CandidateEducationSchema:
        return CandidateEducationSchema(
            id=stored_candidate_education.id,
            school=stored_candidate_education.school,
            major=stored_candidate_education.major,
            description=stored_candidate_education.description,
            start_date=stored_candidate_education.start_date,
            end_date=stored_candidate_education.end_date,
        )
