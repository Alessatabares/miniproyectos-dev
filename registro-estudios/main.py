from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

registros = []
contador = 1

class RegistroIn(BaseModel):
      paciente: str
      protocolo: str
      fecha: str
      hora: str
      doctor: str

@app.post("/registros", status_code=201)
def crear(reg: RegistroIn):
      global contador
      nuevo = {
          "id": contador,
          "paciente": reg.paciente,
          "protocolo": reg.protocolo,
          "fecha": reg.fecha,
          "hora": reg.hora,
          "doctor": reg.doctor,
      }
      registros.append(nuevo)
      contador += 1
      return nuevo

@app.get("/registros")
def listar():
      return registros

@app.get("/registros/{id}")
def obtener(id: int):
      for r in registros:
          if r["id"] == id:
              return r
      raise HTTPException(status_code=404, detail="registro no encontrado")
