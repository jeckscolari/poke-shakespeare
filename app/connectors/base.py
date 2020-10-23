from typing import Any

from aiohttp import ClientSession, ClientResponse



class BaseConnector:
    
    def __init__(self, url: str) -> None:
        self._url = url
        self._session = ClientSession()


    async def _request(self,
                method: str,
                url: str,
                **kwargs: Any) ->  ClientResponse:
                
        return await self._session.request(method=method, url=url, **kwargs)
        