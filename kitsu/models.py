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

from datetime import datetime
from typing import Dict, List, Literal, Optional

import aiohttp
from dateutil.parser import isoparse

__all__ = ("Anime", "Manga")


class Category:
    def __init__(self, data: dict) -> None:
        self._data: dict = data

    def __repr__(self) -> str:
        return f"<Category id={self.id} title='{self.title}'>"

    def __str__(self) -> Optional[str]:
        return self.title

    @property
    def id(self) -> Optional[str]:
        return self._data.get("id", None)

    @property
    def title(self) -> Optional[str]:
        return self._data["attributes"].get("title", None)

    @property
    def created_at(self) -> Optional[datetime]:
        try:
            return isoparse(self._data["attributes"]["createdAt"])
        except (KeyError, TypeError):
            return None

    @property
    def updated_at(self) -> Optional[datetime]:
        try:
            return isoparse(self._data["attributes"]["updatedAt"])
        except (KeyError, TypeError):
            return None

    @property
    def description(self) -> Optional[str]:
        return self._data["attributes"].get("description", None)

    @property
    def total_media_count(self) -> Optional[str]:
        return self._data["attributes"].get("totalMediaCount", None)

    @property
    def nsfw(self) -> Optional[bool]:
        return self._data["attributes"].get("nsfw", None)


class Title:
    def __init__(self, data: dict) -> None:
        self._data: dict = data

    def __repr__(self) -> str:
        value: Optional[str]
        for value in self._data.values():
            if value:
                return value

    def __str__(self) -> str:
        return self.__repr__()

    @property
    def en(self) -> Optional[str]:
        """The english name of the resource"""
        return self._data.get("en", None)

    @property
    def en_jp(self) -> Optional[str]:
        """The japanese name of the resource in english characters"""
        return self._data.get("en_jp", None)

    @property
    def ja_jp(self) -> Optional[str]:
        """The japanese name of the resource"""
        return self._data.get("ja_jp", None)


class Anime:
    def __init__(self, payload: dict, session: aiohttp.ClientSession) -> None:
        self._payload: dict = payload
        self._session: aiohttp.ClientSession = session

    def __repr__(self) -> str:
        return f"<Anime id={self.id} title='{self.title}'>"

    def __str__(self) -> Optional[str]:
        return self.title

    async def _fetch_categories(self) -> Optional[List[Category]]:
        headers = {
            "Accept": "application/vnd.api+json",
            "Content-Type": "application/vnd.api+json",
            "User-Agent": "Kitsu.py (https://github.com/MrArkon/kitsu.py)",
        }
        async with self._session.get(
            url=f"https://kitsu.io/api/edge/anime/{self.id}/categories", headers=headers
        ) as response:
            if response.status == 200:
                _raw_data = await response.json()
            else:
                return None

        return [Category(data) for data in _raw_data["data"]]

    @property
    async def categories(self) -> Optional[List[Category]]:
        return await self._fetch_categories()

    @property
    def id(self) -> Optional[str]:
        return self._payload.get("id", None)

    @property
    def created_at(self) -> Optional[datetime]:
        try:
            return isoparse(self._payload["attributes"]["createdAt"])
        except (KeyError, TypeError):
            return None

    @property
    def updated_at(self) -> Optional[datetime]:
        try:
            return isoparse(self._payload["attributes"]["updatedAt"])
        except (KeyError, TypeError):
            return None

    @property
    def slug(self) -> Optional[str]:
        return self._payload["attributes"].get("slug", None)

    @property
    def synopsis(self) -> Optional[str]:
        return self._payload["attributes"].get("synopsis", None)

    @property
    def title(self) -> Optional[Title]:
        try:
            return Title(self._payload["attributes"]["titles"])
        except (KeyError, TypeError):
            return None

    @property
    def canonical_title(self) -> Optional[str]:
        return self._payload["attributes"].get("canonicalTitle", None)

    @property
    def abbreviated_titles(self) -> Optional[List[str]]:
        return self._payload["attributes"].get("abbreviatedTitles", None)

    @property
    def average_rating(self) -> Optional[float]:
        try:
            return float(self._payload["attributes"]["averageRating"])
        except (KeyError, TypeError):
            return None

    @property
    def rating_frequencies(self) -> Optional[Dict[str, str]]:
        return self._payload["attributes"].get("ratingFrequencies", None)

    @property
    def user_count(self) -> Optional[int]:
        try:
            return int(self._payload["attributes"]["userCount"])
        except (KeyError, TypeError):
            return None

    @property
    def favorites_count(self) -> Optional[int]:
        try:
            return int(self._payload["attributes"]["favoritesCount"])
        except (KeyError, TypeError):
            return None

    @property
    def start_date(self) -> Optional[datetime]:
        try:
            return datetime.strptime(self._payload["attributes"]["startDate"], "%Y-%m-%d")
        except (KeyError, TypeError):
            return None

    @property
    def end_date(self) -> Optional[datetime]:
        try:
            return datetime.strptime(self._payload["attributes"]["endDate"], "%Y-%m-%d")
        except (KeyError, TypeError):
            return None

    @property
    def popularity_rank(self) -> Optional[int]:
        try:
            return int(self._payload["attributes"]["popularityRank"])
        except (KeyError, TypeError):
            return None

    @property
    def rating_rank(self) -> Optional[int]:
        try:
            return int(self._payload["attributes"]["ratingRank"])
        except (KeyError, TypeError):
            return None

    @property
    def age_rating(self) -> Optional[Literal["G", "PG", "R", "R18"]]:
        return self._payload["attributes"].get("ageRating", None)

    @property
    def age_rating_guide(self) -> Optional[str]:
        return self._payload["attributes"].get("ageRatingGuide", None)

    @property
    def subtype(self) -> Optional[Literal["ONA", "OVA", "TV", "movie", "music", "special"]]:
        return self._payload["attributes"].get("subtype", None)

    @property
    def status(self) -> Optional[Literal["current", "finished", "tba", "unreleased", "upcoming"]]:
        return self._payload["attributes"].get("status", None)

    @property
    def tba(self) -> Optional[str]:
        return self._payload["attributes"].get("tba", None)

    def poster_image(
        self, _type: Optional[Literal["tiny", "small", "medium", "large", "original"]] = "original"
    ) -> Optional[str]:
        try:
            return self._payload["attributes"]["posterImage"].get(_type, None)
        except AttributeError:
            return None

    def cover_image(self, _type: Optional[Literal["tiny", "small", "large", "original"]] = "original") -> Optional[str]:
        try:
            return self._payload["attributes"]["coverImage"].get(_type, None)
        except AttributeError:
            return None

    @property
    def episode_count(self) -> Optional[int]:
        try:
            return int(self._payload["attributes"]["episodeCount"])
        except (KeyError, TypeError):
            return None

    @property
    def episode_length(self) -> Optional[int]:
        try:
            return int(self._payload["attributes"]["episodeLength"])
        except (KeyError, TypeError):
            return None

    @property
    def youtube_video_id(self) -> Optional[str]:
        return self._payload["attributes"].get("youtubeVideoId", None)

    @property
    def nsfw(self) -> Optional[bool]:
        return self._payload["attributes"].get("nsfw", None)


class Manga:
    def __init__(self, payload: dict, session: aiohttp.ClientSession) -> None:
        self._payload: dict = payload
        self._session: aiohttp.ClientSession = session

    def __repr__(self) -> str:
        return f"<Manga id={self.id} title='{self.title}'>"

    def __str__(self) -> Optional[str]:
        return self.title

    async def _fetch_categories(self) -> Optional[List[Category]]:
        headers = {
            "Accept": "application/vnd.api+json",
            "Content-Type": "application/vnd.api+json",
            "User-Agent": "Kitsu.py (https://github.com/MrArkon/kitsu.py)",
        }
        async with self._session.get(
            url=f"https://kitsu.io/api/edge/manga/{self.id}/categories", headers=headers
        ) as response:
            if response.status == 200:
                _raw_data = await response.json()
            else:
                return None

        return [Category(data) for data in _raw_data["data"]]

    @property
    async def categories(self) -> Optional[List[Category]]:
        return await self._fetch_categories()

    @property
    def id(self) -> str:
        return self._payload.get("id", None)

    @property
    def created_at(self) -> Optional[datetime]:
        try:
            return isoparse(self._payload["attributes"]["createdAt"])
        except (KeyError, TypeError):
            return None

    @property
    def updated_at(self) -> Optional[datetime]:
        try:
            return isoparse(self._payload["attributes"]["updatedAt"])
        except (KeyError, TypeError):
            return None

    @property
    def slug(self) -> Optional[str]:
        return self._payload["attributes"].get("slug", None)

    @property
    def synopsis(self) -> Optional[str]:
        return self._payload["attributes"].get("synopsis", None)

    @property
    def title(self) -> Optional[Title]:
        try:
            return Title(self._payload["attributes"]["titles"])
        except (KeyError, TypeError):
            return None

    @property
    def canonical_title(self) -> Optional[str]:
        return self._payload["attributes"].get("canonicalTitle", None)

    @property
    def abbreviated_titles(self) -> Optional[List[str]]:
        return self._payload["attributes"].get("abbreviatedTitles", None)

    @property
    def average_rating(self) -> Optional[float]:
        try:
            return float(self._payload["attributes"]["averageRating"])
        except (KeyError, TypeError):
            return None

    @property
    def rating_frequencies(self) -> Optional[Dict[str, str]]:
        return self._payload["attributes"].get("ratingFrequencies", None)

    @property
    def user_count(self) -> Optional[int]:
        try:
            return int(self._payload["attributes"]["userCount"])
        except (KeyError, TypeError):
            return None

    @property
    def favorites_count(self) -> Optional[int]:
        try:
            return int(self._payload["attributes"]["favoritesCount"])
        except (KeyError, TypeError):
            return None

    @property
    def start_date(self) -> Optional[datetime]:
        try:
            return datetime.strptime(self._payload["attributes"]["startDate"], "%Y-%m-%d")
        except (KeyError, TypeError):
            return None

    @property
    def end_date(self) -> Optional[datetime]:
        try:
            return datetime.strptime(self._payload["attributes"]["endDate"], "%Y-%m-%d")
        except (KeyError, TypeError):
            return None

    @property
    def popularity_rank(self) -> Optional[int]:
        try:
            return int(self._payload["attributes"]["popularityRank"])
        except (KeyError, TypeError):
            return None

    @property
    def rating_rank(self) -> Optional[int]:
        try:
            return int(self._payload["attributes"]["ratingRank"])
        except (KeyError, TypeError):
            return None

    @property
    def age_rating(self) -> Optional[Literal["G", "PG", "R", "R18"]]:
        return self._payload["attributes"].get("ageRating", None)

    @property
    def age_rating_guide(self) -> Optional[str]:
        return self._payload["attributes"].get("ageRatingGuide", None)

    @property
    def subtype(self) -> Optional[Literal["doujin", "manga", "manhua", "manhwa", "novel", "oel", "oneshot"]]:
        return self._payload["attributes"].get("subtype", None)

    @property
    def status(self) -> Optional[Literal["current", "finished", "tba", "unreleased", "upcoming"]]:
        return self._payload["attributes"].get("status", None)

    @property
    def tba(self) -> Optional[str]:
        return self._payload["attributes"].get("tba", None)

    def poster_image(
        self, _type: Optional[Literal["tiny", "small", "medium", "large", "original"]] = "original"
    ) -> Optional[str]:
        try:
            return self._payload["attributes"]["posterImage"].get(_type, None)
        except AttributeError:
            return None

    def cover_image(self, _type: Optional[Literal["tiny", "small", "large", "original"]] = "original") -> Optional[str]:
        try:
            return self._payload["attributes"]["coverImage"].get(_type, None)
        except AttributeError:
            return None

    @property
    def chapter_count(self) -> Optional[int]:
        try:
            return int(self._payload["attributes"]["chapterCount"])
        except (KeyError, TypeError):
            return None

    @property
    def volume_count(self) -> Optional[int]:
        try:
            return int(self._payload["attributes"]["volumeCount"])
        except (KeyError, TypeError):
            return None

    @property
    def serialization(self) -> Optional[str]:
        return self._payload["attributes"].get("serialization", None)
