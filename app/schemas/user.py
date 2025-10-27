from pydantic import BaseModel,EmailStr
from typing import Optional, List

class UserBase(BaseModel):
    email: EmailStr

class UserCreate(UserBase):
    password: str

class UserUpdate(BaseModel):
    email: EmailStr | None = None
    password: str | None = None

class UserRead(UserBase):
    id:int
    
    class Config:
        from_attributes = True