from sqlalchemy import CHAR, NVARCHAR, SMALLINT, VARCHAR, Column
from sqlalchemy.dialects.mssql import DATETIMEOFFSET

from src.utils.connector import Base


class CandidateInfo(Base):
    __tablename__ = "candidate_info"

    id = Column(SMALLINT, primary_key=True)
    name = Column(NVARCHAR(50), nullable=False)
    email = Column(VARCHAR(50), nullable=False)
    phone = Column(CHAR(10), nullable=False)
    address = Column(NVARCHAR(100), nullable=False)
    about = Column(NVARCHAR(500), nullable=True, default="")


class CandidateSkill(Base):
    __tablename__ = "candidate_skill"

    id = Column(SMALLINT, primary_key=True)
    candidate_id = Column(SMALLINT, nullable=False)
    name = Column(NVARCHAR(50), nullable=False)
    level = Column(SMALLINT, nullable=False)


class CandidateExperience(Base):
    __tablename__ = "candidate_experience"

    id = Column(SMALLINT, primary_key=True)
    candidate_id = Column(SMALLINT, nullable=False)
    company = Column(NVARCHAR(50), nullable=False)
    position = Column(NVARCHAR(50), nullable=False)
    description = Column(NVARCHAR(100), nullable=True, default="")
    start_date = Column(DATETIMEOFFSET, nullable=False)
    end_date = Column(DATETIMEOFFSET, nullable=True)


class CandidateEducation(Base):
    __tablename__ = "candidate_education"

    id = Column(SMALLINT, primary_key=True)
    candidate_id = Column(SMALLINT, nullable=False)
    school = Column(NVARCHAR(50), nullable=False)
    major = Column(NVARCHAR(50), nullable=False)
    description = Column(NVARCHAR(100), nullable=True, default="")
    start_date = Column(DATETIMEOFFSET, nullable=False)
    end_date = Column(DATETIMEOFFSET, nullable=False)
