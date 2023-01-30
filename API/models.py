from sqlalchemy import Column, Integer, String, DateTime, Boolean

# from datetime import Date
from database import db


class users(db.Model):
    __tablename__ = "users_"
    id = Column(db.Integer, primary_key=True, nullable=False)
    username = Column(db.String, nullable=False, unique=True)
    email = Column(db.String, nullable=False, unique=True)
    password = Column(db.String, nullable=False)
    confirmed = Column(db.Boolean, default=False, nullable=False)

    def __str__(self) -> str:
        return (
            f"Id: {self.id} "
            f"Username: {self.username} "
            f"emial: {self.email} "
            f"confirmed: {self.confirmed}"
        )


class expenses(db.Model):
    __tablename__ = "expenses"
    id = Column(db.Integer, primary_key=True)
    name = Column(db.String)
    type_e = Column(db.Integer)
    description = Column(db.String)
    value = Column(db.Integer, nullable=False)
    data = Column(db.DateTime, nullable=False)
    recursive = Column(db.Boolean, nullable=False, default=False)

    def __str__(self) -> str:
        return {
            f"Id: {self.id} "
            f"Name: {self.name} "
            f"Description: {self.description} "
            f"Value: {self.value} "
            f"Data: {self.data} "
            f"Recursive: {self.recursive}"
        }
