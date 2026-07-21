import bcrypt
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from models import Registro, Usuario
from database import SessionLocal
from seguridad import crear_token, verificar_token
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

app = FastAPI()
security = HTTPBearer()

def usuario_actual(cred:HTTPAuthorizationCredentials = Depends(security)):
      datos = verificar_token(cred.credentials)
      return datos["sub"]

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

@app.post("/login")
def login(user: UsuarioIn):
      db = SessionLocal()
      usuario_db = db.query(Usuario).filter(Usuario.usuario == user.usuario).first()
      db.close()
      if usuario_db is None:
          raise HTTPException(status_code=401, detail="usuario o contraseña incorrectos")
      if not bcrypt.checkpw(user.contrasena.encode(), usuario_db.hash_contrasena.encode()):
          raise HTTPException(status_code=401, detail="usuario o contraseña incorrectos")
      token = crear_token({"sub": usuario_db.usuario})
      return {"access_token": token}


@app.get("/registros")
def listar(usuario: str = Depends(usuario_actual)):
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
