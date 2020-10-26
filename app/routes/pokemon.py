from fastapi import APIRouter, Depends

from app.services.pokemon import PokemonService
from app.models.responses.pokemon import PokemonResponse


router = APIRouter()


@router.get(
    '/{pokemon_name}', 
    response_model=PokemonResponse,
    name='pokemon:get-shakespearean-description',
    responses={
        404: {'description': 'Pokemon not found'},
        502: {'description': 'PokeAPI or Shakespeare translator API error'}})
async def get_shakespearean_description(pokemon_name: str, pokemon_service: PokemonService = Depends(PokemonService)) -> PokemonResponse:
    return await pokemon_service.get_description(pokemon_name=pokemon_name)
