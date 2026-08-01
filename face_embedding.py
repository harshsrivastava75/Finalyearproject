from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import LargeBinary
from sqlalchemy import ForeignKey

from sqlalchemy.orm import relationship

from app.database import Base


class FaceEmbedding(Base):
    __tablename__ = "face_embeddings"

    id = Column(Integer, primary_key=True, index=True)

    student_id = Column(
        Integer,
        ForeignKey("students.id"),
        unique=True
    )

    embedding = Column(
        LargeBinary,
        nullable=False
    )

    student = relationship(
        "Student",
        backref="face_embedding"
    )