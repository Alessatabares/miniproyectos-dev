SECRET_KEY = "2232df78caa11074ab9c5c38bd061511cf6733ae6cd4b3442fd7d575b3977404"
ALGORITHM = "HS256"

import jwt 

from fastapi import HTTPException
from datetime import datetime, timedelta, timezone

def crear_token(datos: dict):
    datos["exp"] = (datetime.now(timezone.utc) + timedelta(minutes=30))
    token = jwt.encode(datos, SECRET_KEY, algorithm=ALGORITHM)
    return token

def verificar_token(token: str):
    try: 
        datos = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return datos
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="token invalido")
    