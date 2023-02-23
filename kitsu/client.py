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

from typing import TYPE_CHECKING, Any, List, Optional

import aiohttp

from . import __version__
from .errors import BadRequest, HTTPException, NotFound
from .models import Anime, Manga

if TYPE_CHECKING:
    from .types import AnimeCollection, AnimeResource, MangaCollection, MangaResource

__all__ = ("Client",)

BASE = "https://kitsu.io/api/edge"
HEADERS = {
    "Accept": "application/vnd.api+json",
    "Content-Type": "application/vnd.api+json",
    "User-Agent": f"Kitsu.py/{__version__} (https://github.com/MrArkon/kitsu.py)",
}


class Client:
    """Represents the client used to interface with the Kitsu API.

    Parameters
    ----------
    session: Optional[:class:`aiohttp.ClientSession`]
        The aiohttp client session to use for performing requests to the Kitsu API.
    """

    __slots__ = ("_session",)

    def __init__(self, session: Optional[aiohttp.ClientSession] = None) -> None:
        self._session = session or aiohttp.ClientSession()

    def __repr__(self) -> str:
        return "<kitsu.Client>"

    async def _request(self, path: str = "", method: str = "GET", **kwargs: Any) -> Any:
        """Internal function used to perform requests to the Kitsu API."""
        kwargs["headers"] = HEADERS

        url = kwargs.pop("url", f"{BASE}/{path}")

        async with self._session.request(method=method, url=url, **kwargs) as response:
            data = await response.json()

            if response.status == 200:
                return data

            if response.status == 400:
                raise BadRequest(response, data["errors"][0]["detail"])
            elif response.status == 404:
                raise NotFound(response, data["errors"][0]["detail"])
            else:
                raise HTTPException(response, await response.text(), response.status)

    async def _insert_filters(self, filters: dict, params: dict) -> None:
        # Credit to @Dymattic for this piece of code.
        for filter_name, filter_value in filters.items():
            param_name = f"filter[{filter_name}]"
            params[param_name] = filter_value

    async def get_anime(self, anime_id: int) -> Anime:
        """
        Fetches an Anime fom the Kitsu API.

        Parameters
        ----------
        anime_id: int
            The UUID of the Anime on Kitsu.

        Returns
        -------
        :class:`Anime`
        """
        data: AnimeResource = await self._request(f"anime/{anime_id}")
        return Anime(data["data"], self)

    async def search_anime(self, query: str = "", limit: int = 1, **filters) -> List[Anime]:
        """
        Searches for Animes from the Kitsu API.

        Parameters
        ----------
        query: str, default: ""
            The query you want to search with
        limit: int, default: 1
            The limit of Animes returned from this request.
        **filters: dict, optional
            The possible filters are: season, season_year, streamers & age_rating

        Returns
        -------
        List[:class:`Anime`]
        """
        params = {"page[limit]": str(limit)}

        if query:
            params["filter[text]"] = query

        await self._insert_filters(filters, params)

        data: AnimeCollection = await self._request("anime", params=params)
        return [Anime(payload, self) for payload in data["data"]]

    async def trending_anime(self) -> List[Anime]:
        """
        Fetches the top 10 trending Animes on Kitsu.

        Returns
        -------
        List[:class:`Anime`]
        """
        data = await self._request("trending/anime")
        return [Anime(payload, self) for payload in data["data"]]

    async def get_manga(self, manga_id: int) -> Manga:
        """
        Fetches a Manga fom the Kitsu API.

        Parameters
        ----------
        manga_id: int
            The UUID of the Manga on Kitsu.

        Returns
        -------
        :class:`Manga`
        """
        data: MangaResource = await self._request(f"manga/{manga_id}")
        return Manga(data["data"], self)

    async def search_manga(self, query: str = "", limit: int = 1, **filters) -> List[Manga]:
        """
        Searches for Mangas from the Kitsu API.

        Parameters
        ----------
        query: str, default: ""
            The query you want to search with.
        limit: int, default: 1
            The limit of Mangas returned from this request.
        **filters: dict, optional
            The possible filters are: season, season_year, streamers & age_rating

        Returns
        -------
        List[:class:`Manga`]
        """
        params = {"page[limit]": str(limit)}

        if query != "":
            params["filter[text]"] = query

        await self._insert_filters(filters, params)

        data: MangaCollection = await self._request("manga", params=params)

        return [Manga(payload, self) for payload in data["data"]]

    async def trending_manga(self) -> List[Manga]:
        """
        Fetches the top 10 trending Mangas on Kitsu.

        Returns
        -------
        List[:class:`Manga`]
        """
        data = await self._request("trending/manga")
        return [Manga(payload, self) for payload in data["data"]]

    async def close(self) -> None:
        """Closes the internal ClientSession."""
        return await self._session.close()
