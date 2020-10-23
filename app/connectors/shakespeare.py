from app.connectors.base import BaseConnector


class ShakespeareConnector(BaseConnector):

    def __init__(self) -> None:
        super().__init__(url='https://api.funtranslations.com/translate/shakespeare.json')


    async def translate_text(self, text: str) -> str:
        response = await self._request(method='POST', url=self._url, params={'text': text})
        body = await response.json()
        print(body)
        translated = body['contents']['translated']

        return translated
