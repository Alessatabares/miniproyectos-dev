# registro-estudios

  API para que (a futuro) estudiantes pasantes registren y consulten estudios de
  investigación: paciente, protocolo, fecha, hora y doctor.
  Parte de `miniproyectos-dev`. Se construye por capas; cada capa agrega un
  concepto.

  ## Cómo correr
      source .venv/bin/activate
      pip install bcrypt          # dependencia de la capa 3 (hashing de contraseñas)
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
  - [ ] Capa 4 — Login + JWT: token y rutas protegidas (autenticación).
  - [ ] Capa 5 — Permisos + relación: cada pasante ve solo lo suyo (autorización
  + FK registro→usuario).

  ## Estructura (capa 2)
  - `database.py` — conexión: engine + SessionLocal (fábrica de sesiones) + Base.
  - `models.py` — modelo `Registro`: la tabla, con `id` como PK autoincremental.
  - `crear_db.py` — crea las tablas en el archivo `.db` (correr una vez).
  - `main.py` — endpoints que leen/escriben en la base con la sesión (add/commit/query).

  ## Dónde quedé
  - Capas 1 y 2 terminadas y probadas (los datos sobreviven al reiniciar).
  - Próximo paso: Capa 3 — usuarios + hashing.
