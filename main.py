from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy import Column, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

# Configuración de la base de datos
SQLALCHEMY_DATABASE_URL = "sqlite:///./users.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Modelo de la tabla usuarios
class UserDB(Base):
    __tablename__ = "users"
    username = Column(String, primary_key=True, index=True)
    password = Column(String)

# Creación de base de datos
Base.metadata.create_all(bind=engine)

# Validación de los datos del usuario
class UserSchema(BaseModel):
    username: str
    password: str

app = FastAPI()

# Dependencia para obtener la sesión de la DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --- ENDPOINTS ---

@app.get("/")
async def root():
    return {"message": "API con SQLite lista para Android"}

@app.post("/register")
def register(user: UserSchema, db: Session = Depends(get_db)):
    # Buscamos si ya existe
    db_user = db.query(UserDB).filter(UserDB.username == user.username).first()
    if db_user:
        return {"message": "usuario ya existe", "status": "error"}
    
    # Si no existe, lo creamos
    new_user = UserDB(username=user.username, password=user.password)
    db.add(new_user)
    db.commit()
    return {"message": "éxito", "status": "ok"}

@app.post("/login")
def login(user: UserSchema, db: Session = Depends(get_db)):
    db_user = db.query(UserDB).filter(UserDB.username == user.username).first()
    
    if db_user and db_user.password == user.password:
        return {
            "message": "Login exitoso",
            "username": db_user.username,
            "status": "success"
        }
    
    raise HTTPException(status_code=401, detail="Credenciales incorrectas")