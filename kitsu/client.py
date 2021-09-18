"""
MIT License

Copyright (c) 2021-present MrArkon

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
from __future__ import annotations

import logging
from typing import Any, List, Optional, Union

import aiohttp

from .models import Anime
from .errors import BadRequest, HTTPException, NotFound

__all__ = ("Client",)
__log__: logging.Logger = logging.getLogger(__name__)

BASE: str = "https://kitsu.io/api/edge"

class Client:
    """User client used to interact with the Kitsu API"""

    def __init__(self, session: Optional[aiohttp.ClientSession] = None) -> None:
        self._session: aiohttp.ClientSession = session or aiohttp.ClientSession()

    async def _get(self, url: str, **kwargs: Any) -> Any:
        """Performs a GET request to the Kitsu API"""

        headers = kwargs.pop("headers", {})

        headers["Accept"] = "application/vnd.api+json"
        headers["Content-Type"] = "application/vnd.api+json"
        headers["User-Agent"] = "Kitsu.py (https://github.com/MrArkon/kitsu.py)"
        kwargs["headers"] = headers

        __log__.debug("Request Headers: %s", headers)
        __log__.debug("Request URL: %s", url)

        async with self._session.get(url=url, **kwargs) as response:
            data = await response.json()
            
            if response.status == 200:
                return data

            if response.status == 400:
                raise BadRequest(response, data["errors"][0]["detail"])
            if response.status == 404:
                raise NotFound(response, data["errors"][0]["detail"])
            else:
                raise HTTPException(response, await response.text(), response.status)

    async def get_anime(self,
                        _id: int,
                        *, raw: bool = False
                        ) -> Union[Anime, List[Anime], dict]:
        """Get information of an anime by ID"""
        data = await self._get(url=f"{BASE}/anime/{_id}")
        
        if raw:
            return data["data"]

        return Anime(data=data["data"])

    async def search_anime(self,
                           query: str,
                           limit: int = 1,
                           *, raw: bool = False
                           ) -> Optional[Union[Anime, List[Anime], dict]]:
        """Search for an anime"""
        data = await self._get(url=f"{BASE}/anime", params={"filter[text]": query, "page[limit]": str(limit)})

        if raw:
            return data

        if not data["data"]:
            return None
        elif len(data["data"]) == 1:
            return Anime(data["data"][0])
        else:
            return [Anime(data=_data) for _data in data["data"]]

    async def trending_anime(self, *, raw: bool = False) -> Optional[Union[List[Anime], dict]]:
        """Get treding anime"""
        data = await self._get(f"{BASE}/trending/anime")
        if raw:
            return data

        if not data["data"]:
            return None
        else:
            return [Anime(data=_data) for _data in data["data"]]

    async def close(self) -> None:
        """Closes the internal http session"""
        return await self._session.close()
