from sqlalchemy import Column, Integer, String
from app.database import Base


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)

    roll_no = Column(String(30), unique=True, nullable=False)

    name = Column(String(150), nullable=False)

    department = Column(String(100))

    semester = Column(String(20))

    email = Column(String(150))

    phone = Column(String(20))

    image_path = Column(String(300))