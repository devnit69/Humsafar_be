from fastapi import FastAPI, APIRouter
from app import db_config


from app.DTO.auth_dto import AuthDto
router = APIRouter()


@router.post('/auth')
def auth_route(req : AuthDto):
    result = db_config.app()
    return result






