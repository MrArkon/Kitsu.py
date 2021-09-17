"""
MIT License

Copyright (c) 2021 MrArkon

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
from typing import Dict, List, Optional, Union

import aiohttp

from kitsu.models import Anime
from kitsu.errors import KitsuError, HTTPException, ServerTimeout

__all__ = ("Client",)
__log__: logging.Logger = logging.getLogger(__name__)

BASE: str = "https://kitsu.io/api/edge"
HEADERS: Dict[str, str] = {
    "Accept": "application/vnd.api+json",
    "Content-Type": "application/vnd.api+json"
}
TIMEOUT_TOTAL = 30.0
TIMEOUT_CONNECT = 20.0


class Client:
    """
    Initialisation
    ~~~~~~~~~~~~~~

    Represents a client connection that connects to Kitsu.io.
    This class is used to interact with the Kitsu.io API
    """

    def __init__(self, session: Optional[aiohttp.ClientSession] = None) -> None:
        if session is not None:
            if not isinstance(session, aiohttp.ClientSession):
                raise ValueError(
                    "`session` must be an `aiohttp.ClientSession` instance")

        self._session: aiohttp.ClientSession = session or aiohttp.ClientSession()

    async def get_anime(self,
                        _id: int,
                        *, raw: bool = False
                        ) -> Union[Anime, List[Anime], dict]:
        """Get information of an anime by ID"""
        try:
            async with self._session.get(
                url=f"{BASE}/anime/{_id}",
                headers=HEADERS,
                timeout=aiohttp.ClientTimeout(total=TIMEOUT_TOTAL, connect=TIMEOUT_CONNECT)
            ) as response:
                data = await response.json()

                if response.status == 200:
                    if raw:
                        return data["data"]

                    return Anime(data=data["data"])

                else:
                    if response.status == 400:
                        raise HTTPException(title=data["errors"][0]["title"],
                                            detail=data["errors"][0]["detail"],
                                            code=400)
                    if response.status == 404:
                        raise HTTPException(title=data["errors"][0]["title"],
                                            detail=data["errors"][0]["detail"],
                                            code=404)

                    raise KitsuError(
                        f"API returned a non 200 status code: {response.status}")

        except aiohttp.ServerTimeoutError:
            raise ServerTimeout(message="Server timed out.")

    async def search_anime(self,
                           query: str,
                           limit: int = 1,
                           *, raw: bool = False
                           ) -> Union[Anime, List[Anime], dict]:
        """Search for an anime"""
        try:
            async with self._session.get(
                url=f"{BASE}/anime",
                headers=HEADERS,
                params={"filter[text]": query, "page[limit]": str(limit)},
                timeout=aiohttp.ClientTimeout(total=TIMEOUT_TOTAL, connect=TIMEOUT_CONNECT)
            ) as response:
                data = await response.json()

                if response.status == 200:
                    if raw:
                        return data

                    if not data["data"]:
                        raise KitsuError("No results found for your query.")
                    elif len(data["data"]) == 1:
                        return Anime(data["data"][0])
                    else:
                        return [Anime(data=_data) for _data in data["data"]]

                else:
                    if response.status == 400:
                        raise HTTPException(title=data["errors"][0]["title"],
                                            detail=data["errors"][0]["detail"],
                                            code=400)
                    if response.status == 404:
                        raise HTTPException(title=data["errors"][0]["title"],
                                            detail=data["errors"][0]["detail"],
                                            code=404)

                    raise KitsuError(
                        f"API returned a non 200 status code: {response.status}")
        except aiohttp.ServerTimeoutError:
            raise ServerTimeout(message="Server timed out.")

    async def trending_anime(self, *, raw: bool = False) -> Union[List[Anime], dict]:
        """Get treding anime"""
        try:
            async with self._session.get(
                url=f"{BASE}/trending/anime",
                headers=HEADERS,
                timeout=aiohttp.ClientTimeout(total=TIMEOUT_TOTAL, connect=TIMEOUT_CONNECT)
            ) as response:
                data = await response.json()

                if response.status == 200:
                    if raw:
                        return data

                    if not data["data"]:
                        raise KitsuError("No results found for your query.")
                    else:
                        return [Anime(data=_data) for _data in data["data"]]

                else:
                    if response.status == 400:
                        raise HTTPException(title=data["errors"][0]["title"],
                                            detail=data["errors"][0]["detail"],
                                            code=400)
                    if response.status == 404:
                        raise HTTPException(title=data["errors"][0]["title"],
                                            detail=data["errors"][0]["detail"],
                                            code=404)

                    raise KitsuError(
                        f"API returned a non 200 status code: {response.status}")
        except aiohttp.ServerTimeoutError:
            raise ServerTimeout(message="Server timed out.")

    async def close(self) -> None:
        """Close the aiohttp ClientSession"""
        await self._session.close()
