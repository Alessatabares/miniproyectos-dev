# registro-estudios

  API para que (a futuro) estudiantes pasantes registren y consulten estudios de
  investigación: paciente, protocolo, fecha, hora y doctor.
  Parte de `miniproyectos-dev`. Se construye por capas; cada capa agrega un
  concepto.

  ## Cómo correr
      source .venv/bin/activate
      uvicorn main:app --reload
      # abrir http://127.0.0.1:8000/docs

  ## Roadmap por capas
  - [ ] Capa 1 — CRUD en RAM: crear/listar/ver registros (POST/GET) + status
  codes. Datos en memoria (se pierden al reiniciar).
  - [ ] Capa 2 — Base de datos (ORM): persistir con SQLite + SQLAlchemy; PK real;
  add/commit.
  - [ ] Capa 3 — Usuarios + hashing: registro de pasantes con contraseña
  hasheada.
  - [ ] Capa 4 — Login + JWT: token y rutas protegidas (autenticación).
  - [ ] Capa 5 — Permisos + relación: cada pasante ve solo lo suyo (autorización
  + FK registro→usuario).

  
