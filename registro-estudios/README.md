# registro-estudios

  API para que (a futuro) estudiantes pasantes registren y consulten estudios de
  investigación: paciente, protocolo, fecha, hora y doctor.
  Parte de `miniproyectos-dev`. Se construye por capas; cada capa agrega un
  concepto.

  ## Cómo correr
      source .venv/bin/activate
      pip install bcrypt          # dependencia de la capa 3 (hashing de contraseñas)
      pip install PyJWT           # dependencia de la capa 4 (tokens JWT)
      python crear_db.py          # solo la 1ª vez: crea las tablas en registro_estudios.db
      uvicorn main:app --reload
      # abrir http://127.0.0.1:8000/docs

  ## Roadmap por capas
  - [x] Capa 1 — CRUD en RAM: crear/listar/ver registros (POST/GET) + status
  codes. Datos en memoria (se pierden al reiniciar).
  - [x] Capa 2 — Base de datos (ORM): persistir con SQLite + SQLAlchemy; PK real;
  add/commit.
  - [x] Capa 3 — Usuarios + hashing: registro de pasantes con contraseña
  hasheada (bcrypt + sal). La contraseña en texto plano nunca se guarda.
  - [x] Capa 4 — Login + JWT: token y rutas protegidas (autenticación).
  - [ ] Capa 5 — Permisos + relación: cada pasante ve solo lo suyo (autorización
  + FK registro→usuario).

  ## Estructura
  - `database.py` — conexión: engine + SessionLocal (fábrica de sesiones) + Base.
  - `models.py` — modelos `Registro` y `Usuario` (con `hash_contrasena`).
  - `crear_db.py` — crea las tablas en el archivo `.db` (correr una vez).
  - `seguridad.py` — caja de herramientas de JWT: `crear_token` (firma) y
    `verificar_token` (valida firma y caducidad, lanza 401 si falla).
  - `main.py` — endpoints, el "guardia" `usuario_actual` y los moldes (Pydantic).

  ## Dónde quedé
  - Capas 1 a 4 terminadas y probadas.
  - Capa 4: `seguridad.py` (SECRET_KEY, ALGORITHM, `crear_token`, `verificar_token`),
    endpoint `POST /login` que entrega el JWT, y `GET /registros` protegido con
    `Depends(usuario_actual)`. Probado: sin token → 401, token falso → 401,
    token válido → 200.
  - Próximo paso: Capa 5 — permisos + relación (cada pasante ve solo lo suyo).
