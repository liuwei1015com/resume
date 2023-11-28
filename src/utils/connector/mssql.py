from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, declarative_base, sessionmaker

from src.configs import DB_DATABASE, DB_DRIVER, DB_PASSWORD, DB_PORT, DB_SERVER, DB_URI, DB_USER


class Base:
    __allow_unmapped__ = True


DB_URL: str = f"{DB_URI}://{DB_USER}:{DB_PASSWORD}@{DB_SERVER}:{DB_PORT}/{DB_DATABASE}?driver={DB_DRIVER}"

engine = create_engine(DB_URL, echo=False)

Base: DeclarativeBase = declarative_base(cls=Base)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    session = SessionLocal()
    try:
        yield session
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()
