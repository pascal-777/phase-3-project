from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base
from .password_entry import PasswordEntry

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    
    password_entries = relationship('PasswordEntry', back_populates='user', cascade='all, delete-orphan')
    
    def __repr__(self):
        return f"<User(username='{self.username}', email='{self.email}')>"

    @property
    def secure_password(self):
        return '*' * len(self.password)

    @staticmethod
    def create(session, username, password, email):
        user = User(username=username, password=password, email=email)
        session.add(user)
        session.commit()
        return user

    @staticmethod
    def delete(session, user_id):
        user = session.query(User).filter_by(id=user_id).first()
        if user:
            session.delete(user)
            session.commit()

    @staticmethod
    def get_all(session):
        return session.query(User).all()

    @staticmethod
    def find_by_id(session, user_id):
        return session.query(User).filter_by(id=user_id).first()

    @staticmethod
    def find_by_username(session, username):
        return session.query(User).filter_by(username=username).first()
