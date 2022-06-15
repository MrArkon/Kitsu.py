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

from .errors import BadRequest, HTTPException, NotFound
from .models import Anime, Character, Manga

__all__ = ("Client",)
__log__: logging.Logger = logging.getLogger(__name__)

BASE: str = "https://kitsu.io/api/edge"


class Client:
    """User client used to interact with the Kitsu API"""

    def __init__(self, session: Optional[aiohttp.ClientSession] = None) -> None:
        self._session: aiohttp.ClientSession = session or aiohttp.ClientSession()

    def __repr__(self) -> str:
        return "<kitsu.Client>"

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

            raise HTTPException(response, await response.text(), response.status)

    async def _insert_filters(self, filters: dict, params: dict) -> None:
        # Credit to @Dymattic for this piece of code.
        for filter_name, filter_value in filters.items():
            param_name = f"filter[{filter_name}]"
            params[param_name] = filter_value

    async def get_anime(self, anime_id: int, *, raw: bool = False) -> Union[Anime, dict]:
        """
        Fetch the information of an anime using its ID

        Parameters
        ----------
        anime_id: int
            The ID of the Anime
        raw: bool, default: False
            Whether to return the information in a dict

        Returns
        -------
        Union[:class:`Anime`, :class:`dict`]
            An :class:`Anime` instance, If the raw parameter is True it will return the raw json information by the API
        """
        data = await self._get(url=f"{BASE}/anime/{anime_id}")

        if raw:
            return data

        return Anime(data["data"], self._session)

    async def search_anime(
        self, query: str = "", limit: int = 1, *, raw: bool = False, **filters
    ) -> Optional[Union[Anime, List[Anime], dict]]:
        """
        Search for an Anime with its Name or Filters

        Parameters
        ----------
        query: str, default: ""
            The query you want to search with
        limit: int, default: 1
            Limits the number of animes returned
        raw: bool, default: False
            Whether to return the information in a dict
        **filters: dict, optional
            The possible filters are: season, season_year, streamers & age_rating

        Returns
        -------
        Optional[Union[Anime, List[Anime], dict]]
            An :class:`Anime` instance if only one result is found or the limit is 1, Multiple :class:`Anime` instances otherwise.
            If the raw parameter is True it will return the raw json information by the API.
        """
        params = {"page[limit]": str(limit)}

        if query != "":
            params["filter[text]"] = query

        await self._insert_filters(filters, params)

        data = await self._get(url=f"{BASE}/anime", params=params)

        if raw:
            return data

        if not data["data"]:
            return None
        elif len(data["data"]) == 1:
            return Anime(data["data"][0], self._session)
        else:
            return [Anime(payload, self._session) for payload in data["data"]]

    async def trending_anime(self, *, raw: bool = False) -> Optional[Union[List[Anime], dict]]:
        """
        Fetch trending animes

        Parameters
        ----------
        raw: bool, default: False
            Whether to return the information in a dict

        Returns
        -------
        Optional[Union[List[Anime], dict]]
            A list of :class:`Anime` instances. If the raw parameter is True it will return the raw json information by the API
        """
        data = await self._get(f"{BASE}/trending/anime")
        if raw:
            return data

        if not data["data"]:
            return None
        else:
            return [Anime(payload, self._session) for payload in data["data"]]

    async def get_manga(self, manga_id: int, *, raw: bool = False) -> Union[Manga, dict]:
        """
        Fetch the information of a manga using its ID

        Parameters
        ----------
        manga_id: int
            The ID of the manga
        raw: bool, default: False
            Whether to return the information in a dict

        Returns
        -------
        Union[:class:`Manga`, :class:`dict`]
            An :class:`Manga` instance, If the raw parameter is True it will return the raw json information by the API
        """
        data = await self._get(url=f"{BASE}/manga/{manga_id}")

        if raw:
            return data["data"]

        return Manga(data["data"], self._session)

    async def search_manga(
        self, query: str = "", limit: int = 1, *, raw: bool = False, **filters
    ) -> Optional[Union[Manga, List[Manga], dict]]:
        """
        Search for a Manga with its Name or Filters

        Parameters
        ----------
        query: str, default: ""
            The query you want to search with
        limit: int, default: 1
            Limits the number of mangas returned
        raw: bool, default: False
            Whether to return the information in a dict
        **filters: dict, optional
            The possible filters are: season, season_year, streamers & age_rating

        Returns
        -------
        Optional[Union[Anime, List[Manga], dict]]
            A :class:`Manga` instance if only one result is found or the limit is 1, Multiple :class:`Manga` instances otherwise.
            If the raw parameter is True it will return the raw json information by the API.
        """
        params = {"page[limit]": str(limit)}

        if query != "":
            params["filter[text]"] = query

        await self._insert_filters(filters, params)

        data = await self._get(url=f"{BASE}/manga", params=params)

        if raw:
            return data

        if not data["data"]:
            return None
        elif len(data["data"]) == 1:
            return Manga(data["data"][0], self._session)
        else:
            return [Manga(payload, self._session) for payload in data["data"]]

    async def get_character(self, character_id: int, *, raw: bool = False) -> Union[Character, dict]:
        """
        Fetch the information of a character using its ID

        Parameters
        ----------
        character_id: int
            The ID of the manga
        raw: bool, default: False
            Whether to return the information in a dict

        Returns
        -------
        Union[:class:`Character`, :class:`dict`]
            An :class:`Character` instance, If the raw parameter is True it will return the raw json information by the API
        """
        data = await self._get(url=f"{BASE}/characters/{character_id}")

        if raw:
            return data["data"]

        return Character(data["data"], self._session)

    async def search_character(
        self, query: str = "", limit: int = 1, *, raw: bool = False, **filters
    ) -> Optional[Union[Character, List[Character], dict]]:
        """
        Search for a character with its Name or Filters

        Parameters
        ----------
        query: str, default: ""
            The query you want to search with
        limit: int, default: 1
            Limits the number of character returned
        raw: bool, default: False
            Whether to return the information in a dict
        **filters: dict, optional
            The possible filters are: name, slug

        Returns
        -------
        Optional[Union[Character, List[Character], dict]]
            A :class:`Character` instance if only one result is found or the limit is 1, Multiple :class:`Character` instances otherwise.
            If the raw parameter is True it will return the raw json information by the API.
        """
        params = {"page[limit]": str(limit)}

        if query != "":
            params["filter[name]"] = query

        await self._insert_filters(filters, params)

        data = await self._get(url=f"{BASE}/characters", params=params)

        if raw:
            return data

        if not data["data"]:
            return None
        elif len(data["data"]) == 1:
            return Character(data["data"][0], self._session)
        else:
            return [Character(payload, self._session) for payload in data["data"]]

    async def trending_manga(self, *, raw: bool = False) -> Optional[Union[List[Manga], dict]]:
        """
        Fetch trending Mangas

        Parameters
        ----------
        raw: bool, default: False
            Whether to return the information in a dict

        Returns
        -------
        Optional[Union[List[Manga], dict]]
            A list of :class:`Manga` instances. If the raw parameter is True it will return the raw json information by the API
        """
        data = await self._get(f"{BASE}/trending/manga")
        if raw:
            return data

        if not data["data"]:
            return None
        else:
            return [Manga(payload, self._session) for payload in data["data"]]

    async def close(self) -> None:
        """Closes the internal http session"""
        return await self._session.close()
