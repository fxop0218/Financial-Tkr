from sqlalchemy import Column, Integer, String, DateTime, Boolean

# from datetime import Date
from database import Base


# class Users(BaseModel):
#     id: int
#     username: str
#     email: str
#     password: str


class users(Base):
    __tablename__ = "Users_"
    id = Column(Integer, primary_key=True, nullable=False)
    username = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    confirmed = Column(Boolean, default=False, nullable=False)


class expenses(Base):
    __tablename__ = "Expenses"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    type_e = Column(Integer)
    description = Column(String)
    value = Column(Integer, nullable=False)
    data = Column(DateTime, nullable=False)
    recursive = Column(Boolean, nullable=False, default=False)
