#este documento será el encargado de interactuar con la base de datos
from typing import Optional
from pydantic import BaseModel, Field, EmailStr
from uuid import UUID, uuid4#generar ID V4 (aleatoriamente)
from beanie import Document, Indexed

class User(BaseModel):
    ##user_id: UUID = Field(default_factory=uuid4)
    ##username: Indexed(str, unique=True)
    ##email: Indexed(EmailStr, unique=True)
    id: Optional[str]
    name: str
    email: str
    password: str