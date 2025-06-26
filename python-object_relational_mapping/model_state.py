#!/usr/bin/python3
"""
Définition de la classe State avec SQLAlchemy
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Création de l'instance de base déclarative
Base = declarative_base()

class State(Base):
    """
    Classe State qui hérite de Base et correspond à la table 'states'
    """
    __tablename__ = 'states'
    
    # Définition des colonnes
    id = Column(
        Integer, 
        primary_key=True,    # Clé primaire
        autoincrement=True,  # Auto-incrémentation
        nullable=False       # Ne peut pas être NULL
    )
    
    name = Column(
        String(128),         # Chaîne de max 128 caractères
        nullable=False        # Ne peut pas être NULL
    )
