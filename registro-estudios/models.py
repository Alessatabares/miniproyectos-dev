from sqlalchemy import Column, Integer, String
from database import Base

class Registro(Base):
    __tablename__ = "registros"
    id = Column(Integer, primary_key=True)
    paciente = Column(String)
    protocolo = Column(String)
    fecha = Column(String)
    hora = Column(String)
    doctor = Column(String)

class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True)
    usuario = Column(String, unique=True)
    hash_contrasena = Column(String)