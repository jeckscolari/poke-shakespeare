from typing import Any
from requests import request, Response


class BaseConnector:
    
    def __init__(self, url: str) -> None:
        self._url = url
        

    def _request(self,
                method: str,
                url: str,
                **kwargs: Any) ->  Response:
        
        return request(method=method, url=url, **kwargs)
        