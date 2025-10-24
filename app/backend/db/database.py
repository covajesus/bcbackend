from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 🔵 Conexión a la base principal
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://admin:Chile2025@jisbackend.com:3306/blackcathostal"
engine = create_engine(SQLALCHEMY_DATABASE_URI, pool_size=20, max_overflow=0, echo=False)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()