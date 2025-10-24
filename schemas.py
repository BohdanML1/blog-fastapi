from pydantic import BaseModel, EmailStr, constr
from typing import Optional
from datetime import datetime

# ----- Users -----
class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserCreate(UserBase):
    password: constr(min_length=8, max_length=72)  # <=72 символи

class UserOut(UserBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True

# ----- Token -----
class Token(BaseModel):
    access_token: str
    token_type: str

# ----- Posts -----
class PostBase(BaseModel):
    title: str
    content: str

class PostCreate(PostBase):
    pass

class PostUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None

class PostOut(PostBase):
    id: int
    owner_id: int
    created_at: datetime

    class Config:
        from_attributes = True
