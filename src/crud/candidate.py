from src.models import CandidateEducation, CandidateExperience, CandidateInfo, CandidateSkill
from src.utils.connector import Session


class CandidateInfoCRUD:
    @staticmethod
    def read_candidate_info_by_name(name: str, db: Session):
        stored_candidate_info = db.query(CandidateInfo).filter_by(name=name).first()
        return stored_candidate_info


class CandidateSkillCRUD:
    @staticmethod
    def read_candidate_skills_by_candidate_id(candidate_id: int, db: Session):
        stored_candidate_skills = db.query(CandidateSkill).filter_by(candidate_id=candidate_id).all()
        return stored_candidate_skills


class CandidateExperienceCRUD:
    @staticmethod
    def read_candidate_experiences_by_candidate_id(candidate_id: int, db: Session):
        stored_candidate_experiences = db.query(CandidateExperience).filter_by(candidate_id=candidate_id).all()
        return stored_candidate_experiences


class CandidateEducationCRUD:
    @staticmethod
    def read_candidate_educations_by_candidate_id(candidate_id: int, db: Session):
        stored_candidate_educations = db.query(CandidateEducation).filter_by(candidate_id=candidate_id).all()
        return stored_candidate_educations
