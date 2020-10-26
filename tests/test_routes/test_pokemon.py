from unittest.mock import patch

from fastapi.testclient import TestClient
from fastapi import HTTPException

from app.main import app
from app.services.pokemon import PokemonService
from app.models.domain.pokemon import Pokemon

from tests.utils import AsyncMock


def test_existing_pokemon():
    with patch.object(PokemonService, 'get_description', new_callable=AsyncMock, return_value=Pokemon(name='test', description='test')):
        client = TestClient(app)

        response = client.get('/pokemon/test')
        assert response.status_code == 200
        assert response.json() == {
            'name': 'test',
            'description': 'test'
        }


def test_non_existing_pokemon():
    with patch.object(PokemonService, 'get_description', new_callable=AsyncMock, side_effect=HTTPException(status_code=404, detail='Pokemon not found')):
        client = TestClient(app)

        response = client.get('/pokemon/test')
        assert response.status_code == 404
        assert response.json() == {
            'detail': 'Pokemon not found',
        }