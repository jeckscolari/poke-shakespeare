from fastapi import APIRouter

from app.services.pokemon import PokemonService

router = APIRouter()

pokemon_service = PokemonService()


@router.get('/{pokemon_name}')
async def get_shakespearean_description(pokemon_name: str) -> str:
    return await pokemon_service.get_shakespearean_description(pokemon_name=pokemon_name)
