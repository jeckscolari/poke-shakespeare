from fastapi import APIRouter

from app.routes import pokemon


router = APIRouter()
router.include_router(pokemon.router, tags=['pokemon'], prefix='/pokemon')
