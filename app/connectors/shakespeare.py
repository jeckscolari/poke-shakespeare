from fastapi import HTTPException

from app.connectors.base import BaseConnector


class ShakespeareConnector(BaseConnector):

    def __init__(self) -> None:
        super().__init__(url='https://api.funtranslations.com/translate/shakespeare.json')


    def translate_text(self, text: str) -> str:
        response = self._request(method='POST', url=self._url, data={'text': text})
        try:
            body = response.json()
            translated = body['contents']['translated']
            return translated
        except Exception:
            raise HTTPException(status_code=502, detail='Something went wrong translating text')