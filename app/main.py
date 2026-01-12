from fastapi import FastAPI
from app.core.database import Base, engine
from app.routes import auth

Base.metadata.create_all(bind=engine)

app = FastAPI(title="EduRDC API")

app.include_router(auth.router)

@app.get("/")
def root():
    return {"message": "EduRDC Backend is running"}
