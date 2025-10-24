from pydantic import BaseModel, Field, EmailStr
from fastapi import UploadFile, File
from typing import Union, List, Dict, Optional
from datetime import datetime
from decimal import Decimal
from fastapi import Form
from typing import List
from typing import Optional

class UserLogin(BaseModel):
    id: Union[int, None]
    rol_id: Union[int, None]
    rut: Union[int, None]
    branch_office_id: Union[int, None]
    full_name: Union[str, None]
    email: Union[str, None]
    phone: Union[str, None]
    hashed_password: Union[str, None]

class RecoverPassword(BaseModel):
    phone: Union[int, None]
    new_password: Union[str, None]

class RecoverUser(BaseModel):
    rut: str
    email: str

class User(BaseModel):
    rol_id: int
    branch_office_id: Union[int, None]
    rut: str
    full_name: str
    email: str
    password: str
    phone: str

class UpdateUser(BaseModel):
    rol_id: int = None
    rut: str = None
    full_name: str = None
    email: str = None
    phone: str = None

class Rol(BaseModel):
    rol: str
    added_date: datetime
    updated_date: Union[datetime, None]

class UpdateRol(BaseModel):
    rol: str = None
    updated_date: Union[datetime, None]

class ConfirmEmail(BaseModel):
    visual_rut: str = None
    personal_email: str = None
    updated_date: Union[datetime, None]

class UserList(BaseModel):
    rut: Optional[str] = None  # Ahora es opcional
    page: int
