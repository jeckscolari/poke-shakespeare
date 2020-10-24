from fastapi import APIRouter, Depends

from app.services.pokemon import PokemonService
from app.models.responses.pokemon import PokemonResponse


router = APIRouter()


@router.get('/{pokemon_name}', response_model=PokemonResponse)
def get_shakespearean_description(pokemon_name: str, pokemon_service: PokemonService = Depends(PokemonService)) -> PokemonResponse:
    pokemon = pokemon_service.get_shakespearean_description(pokemon_name=pokemon_name)
    return PokemonResponse(name=pokemon.name, description=pokemon.description)
