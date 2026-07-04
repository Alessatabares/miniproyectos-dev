from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from models import Registro
from database import SessionLocal

app = FastAPI()

class RegistroIn(BaseModel):
      paciente: str
      protocolo: str
      fecha: str
      hora: str
      doctor: str

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