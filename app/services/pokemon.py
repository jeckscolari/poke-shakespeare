from app.services.base import BaseService
from app.connectors.shakespeare import ShakespeareConnector


class PokemonService(BaseService):
    
    def __init__(self) -> None:
        super().__init__()
        self._shakespeare_connector = ShakespeareConnector()


    async def get_shakespearean_description(self, pokemon_name: str) -> str:
        return await self._shakespeare_connector.translate_text(pokemon_name)
