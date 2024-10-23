
from sqlalchemy import Column, Integer, String, Text, Date, ForeignKey
from sqlalchemy.orm import relationship
from app import db



class Realisateur(db.Model):
    __tablename__ = 'realisateur'
    
    id = Column(Integer, primary_key=True)
    nom = Column(String(100), nullable=False)
    prenom = Column(String(100), nullable=False)
    
    films = relationship('Film', back_populates='realisateur')

class Film(db.Model):
    __tablename__ = 'film'
    
    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=True)
    release_date = Column(Date, nullable=True)
    realisateur_id = Column(Integer, ForeignKey('realisateur.id'), nullable=True)
    
    realisateur = relationship('Realisateur', back_populates='films')
