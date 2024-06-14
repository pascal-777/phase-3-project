from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class PasswordEntry(Base):
    __tablename__ = 'password_entries'
    
    id = Column(Integer, primary_key=True)
    site_name = Column(String, nullable=False)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    
    user = relationship('User', back_populates='password_entries')

    def __repr__(self):
        return f"<PasswordEntry(site_name='{self.site_name}', username='{self.username}')>"

    @staticmethod
    def create(session, site_name, username, password, user_id):
        entry = PasswordEntry(site_name=site_name, username=username, password=password, user_id=user_id)
        session.add(entry)
        session.commit()
        return entry

    @staticmethod
    def delete(session, entry_id):
        entry = session.query(PasswordEntry).filter_by(id=entry_id).first()
        if entry:
            session.delete(entry)
            session.commit()

    @staticmethod
    def get_all(session):
        return session.query(PasswordEntry).all()

    @staticmethod
    def find_by_id(session, entry_id):
        return session.query(PasswordEntry).filter_by(id=entry_id).first()
