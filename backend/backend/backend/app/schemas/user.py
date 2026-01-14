from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    nom: str
    prenom: str
    email: EmailStr
    password: str
    role: str

class UserOut(BaseModel):
    id: int
    nom: str
    prenom: str
    email: EmailStr
    role: str

    class Config:
        #orm_mode = True
        from_attributes = True
