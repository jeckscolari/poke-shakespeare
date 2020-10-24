from fastapi import HTTPException

from app.connectors.base import BaseConnector


class PokemonConnector(BaseConnector):

    def __init__(self) -> None:
        super().__init__(url='https://pokeapi.co/api/v2')


    def get_pokemon_description(self, pokemon_name: str) -> str:
        url = '{}/pokemon-species/{}'.format(self._url, pokemon_name)
        response = self._request(method='GET', url=url)
        if response.status_code == 404:
            raise HTTPException(status_code=404, detail='Pokemon {} not found'.format(pokemon_name))
        try:
            body = response.json()
            description = next(d for d in body['flavor_text_entries'] if d['language']['name'] == 'en')
            return description['flavor_text']
        except Exception:
            raise HTTPException(status_code=502, detail='Something went wrong retrieving pokemon description')