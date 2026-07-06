import bcrypt
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from models import Registro, Usuario
from database import SessionLocal

app = FastAPI()

class RegistroIn(BaseModel):
      paciente: str
      protocolo: str
      fecha: str
      hora: str
      doctor: str

class UsuarioIn(BaseModel):
      usuario: str
      contrasena: str

@app.post("/registros", status_code=201)
def crear(reg: RegistroIn):
      db = SessionLocal()
      nuevo = Registro(
            paciente=reg.paciente,
            protocolo=reg.protocolo,
            fecha=reg.fecha,
            hora=reg.hora,
            doctor=reg.doctor,
      )
      db.add(nuevo)
      db.commit()
      db.refresh(nuevo)
      db.close()
      return nuevo

@app.post("/usuarios", status_code=201)
def crear_usuario(user: UsuarioIn):
      db = SessionLocal()
      hash_bytes = bcrypt.hashpw(user.contrasena.encode(), bcrypt.gensalt())
      nuevo_usuario = Usuario(
            usuario=user.usuario,
            hash_contrasena=hash_bytes.decode()
      )
      db.add(nuevo_usuario)   
      db.commit()
      db.refresh(nuevo_usuario)
      db.close()
      return nuevo_usuario


@app.get("/registros")
def listar():
      db = SessionLocal()
      registros = db.query(Registro).all()
      db.close()
      return registros

@app.get("/registros/{id}")
def obtener(id: int):
      db = SessionLocal()
      registro = db.query(Registro).filter(Registro.id == id).first()
      db.close()
      if registro is None:
          raise HTTPException(status_code=404, detail="registro no encontrado")
      return registro