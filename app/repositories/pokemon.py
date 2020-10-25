from typing import Optional

from aioredis import Redis

from app.repositories.base import BaseRepository
from app.models.domain.pokemon import Pokemon

class PokemonRepository(BaseRepository):
    
    def __init__(self, conn: Redis):
        super().__init__(conn)


    async def get_description(self, pokemon_name: str) -> Optional[Pokemon]:
        description = await self._conn.get(pokemon_name)
        if description:
            return Pokemon(name=pokemon_name, description=description)


    async def set_description(self, pokemon: Pokemon) -> None:
        await self._conn.set(pokemon.name, pokemon.description)