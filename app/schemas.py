from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import Optional, Annotated

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True
    
class PostCreate(PostBase):
    pass

class Post(PostBase):
    id: int
    owner: UserOut
    owner_id: int
    created_at: datetime
    
    class Config:
        from_attributes = True
        
class PostOut(BaseModel):
    Post: Post
    votes: int
        
        
class UserCreate(BaseModel):
    email: EmailStr
    password: str
    
class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime
    
    class Config:
        from_attributes = True
        
class UserLogin(BaseModel):
    email: EmailStr
    password: str
    
class Token(BaseModel):
    access_token: str
    token_type: str
    
class TokenData(BaseModel):
    id: Optional[int] = None
    
class Vote(BaseModel):
    post_id: int
    dir: Annotated[int, Field(ge=0, le=1)]