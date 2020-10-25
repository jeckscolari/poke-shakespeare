from typing import Optional

from fastapi import Depends

from app.services.base import BaseService
from app.models.domain.pokemon import Pokemon
from app.connectors.shakespeare import ShakespeareConnector
from app.connectors.pokemon import PokemonConnector 
from app.repositories.pokemon import PokemonRepository
from app.repositories.base import get_repository


class PokemonService(BaseService):
    
    def __init__(self,
                shakespeare_connector: ShakespeareConnector = Depends(ShakespeareConnector),
                pokemon_connector: PokemonConnector = Depends(PokemonConnector),
                pokemon_repository: PokemonRepository = Depends(get_repository(PokemonRepository))) -> None:

        super().__init__()
        self._shakespeare_connector = shakespeare_connector
        self._pokemon_connector = pokemon_connector
        self._pokemon_repository = pokemon_repository


    async def get_description(self, pokemon_name: str) -> Pokemon:
        cached = await self._get_cached_description(pokemon_name)
        if cached:
            return cached
        else:
            pokemon_description = self._pokemon_connector.get_pokemon_description(pokemon_name=pokemon_name)
            shakespearean_description = self._shakespeare_connector.translate_text(text=pokemon_description)
            pokemon = Pokemon(name=pokemon_name, description=shakespearean_description)
            await self._cache_description(pokemon)
            return pokemon


    async def _get_cached_description(self, pokemon_name: str) -> Pokemon:
        if self._pokemon_repository:
            return await self._pokemon_repository.get_description(pokemon_name)
    

    async def _cache_description(self, pokemon: Pokemon) -> None:
        if self._pokemon_repository:
            return await self._pokemon_repository.set_description(pokemon)