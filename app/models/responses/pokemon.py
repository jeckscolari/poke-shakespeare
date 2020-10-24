from pydantic import BaseModel


class PokemonResponse(BaseModel):
    name: str
    description: str
