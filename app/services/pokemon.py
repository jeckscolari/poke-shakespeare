from fastapi import Depends

from app.services.base import BaseService
from app.models.domain.pokemon import Pokemon
from app.connectors.shakespeare import ShakespeareConnector
from app.connectors.pokemon import PokemonConnector 


class PokemonService(BaseService):
    
    def __init__(self,
                shakespeare_connector: ShakespeareConnector = Depends(ShakespeareConnector),
                pokemon_connector: PokemonConnector = Depends(PokemonConnector)) -> None:

        super().__init__()
        self._shakespeare_connector = shakespeare_connector
        self._pokemon_connector = pokemon_connector


    def get_shakespearean_description(self, pokemon_name: str) -> Pokemon:
        pokemon_description = self._pokemon_connector.get_pokemon_description(pokemon_name=pokemon_name)
        shakespearean_description = self._shakespeare_connector.translate_text(text=pokemon_description)
        return Pokemon(name=pokemon_name, description=shakespearean_description)