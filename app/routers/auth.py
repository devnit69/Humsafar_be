from fastapi import FastAPI, APIRouter, Depends, HTTPException
from app import db_config
from sqlalchemy.orm import Session

from app.DTO.auth_dto import AuthDto
from app.db.schemas import RegisterSchema
from app.db import models, connection, schemas
from app.core import security


router = APIRouter()


def get_db():
    db = connection.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post('/register')
def register(data: RegisterSchema, db: Session = Depends(get_db)):
    existing_user = db.query(models.User).filter(models.User.email == data.email).first()
    if existing_user:
        raise HTTPException(status_code=409, detail='Email already registered')
    user = models.User(
        email = data.email,
        full_name = data.full_name,
        hashed_password = security.hash_password(data.password)
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    import smtplib
    from email.message import EmailMessage
    msg = EmailMessage()
    msg.set_content('Test Content')
    msg['From'] = me
    return data




