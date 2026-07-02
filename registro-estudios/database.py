from sqlalchemy import create_engine
engine = create_engine('sqlite:///registro_estudios.db', echo=True)