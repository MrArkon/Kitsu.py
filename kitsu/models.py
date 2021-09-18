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

from typing import List, Literal, Optional

from dateutil.parser import isoparse
from datetime import datetime

__all__ = ("Anime",)


class Anime:

    def __init__(self, data: dict) -> None:
        self._data: dict = data

    def __repr__(self) -> str:
        return f"<Anime id={self.id} title='{self.title}'>"

    @property
    def id(self) -> Optional[int]:
        """The anime's ID."""
        return self._data.get("id", None)

    @property
    def created_at(self) -> Optional[datetime]:
        """
        Returns creation datetime
        """
        try:
            return isoparse(self._data["attributes"]["createdAt"])
        except KeyError:
            return None

    @property
    def updated_at(self) -> Optional[datetime]:
        """
        Returns the last modified datetime
        """
        try:
            return isoparse(self._data["attributes"]["updatedAt"])
        except KeyError:
            return None

    @property
    def slug(self) -> Optional[str]:
        return self._data["attributes"].get("slug", None)

    @property
    def synopsis(self) -> Optional[str]:
        return self._data["attributes"].get("synopsis", None)

    @property
    def title(self) -> str:
        """The anime's title."""
        title = self._data["attributes"]["titles"].get("en", None)
        if title is None:
            k = next(iter(self._data["attributes"]["titles"]))
            return self._data["attributes"]["titles"][k]
        return title

    @property
    def canonical_title(self) -> Optional[str]:
        return self._data["attributes"].get("canonicalTitle", None)

    @property
    def abbreviated_titles(self) -> Optional[List[str]]:
        return self._data["attributes"].get("abbreviatedTitles", None)

    @property
    def average_rating(self) -> Optional[float]:
        try:
            return float(self._data["attributes"]["averageRating"])
        except KeyError or TypeError:
            return None

    @property
    def rating_frequencies(self) -> Optional[str]:
        try:
            return str(self._data["attributes"]["ageRating"])
        except KeyError:
            return None

    @property
    def user_count(self) -> Optional[int]:
        try:
            return int(self._data["attributes"]["userCount"])
        except KeyError:
            return None

    @property
    def favorites_count(self) -> Optional[int]:
        try:
            return int(self._data["attributes"]["favoritesCount"])
        except KeyError:
            return None

    @property
    def start_date(self) -> Optional[datetime]:
        try:
            return datetime.strptime(self._data["attributes"]["startDate"], "%Y-%m-%d")
        except KeyError:
            return None

    @property
    def end_date(self) -> Optional[datetime]:
        """Returns the end date as a datetime object"""
        try:
            return datetime.strptime(self._data["attributes"]["endDate"], "%Y-%m-%d")
        except KeyError:
            return None

    @property
    def popularity_rank(self) -> Optional[int]:
        try:
            return int(self._data["attributes"]["popularityRank"])
        except KeyError:
            return None

    @property
    def rating_rank(self) -> Optional[int]:
        try:
            return int(self._data["attributes"]["ratingRank"])
        except KeyError:
            return None

    @property
    def age_rating_guide(self) -> Optional[str]:
        return self._data["attributes"].get("ageRatingGuide", None)

    @property
    def subtype(self) -> Optional[str]:
        try:
            return str(self._data["attributes"]["subtype"])
        except KeyError:
            return None

    @property
    def status(self) -> Optional[str]:
        try:
            return str(self._data["attributes"]["status"])
        except KeyError:
            return None

    @property
    def tba(self) -> Optional[str]:
        return self._data["attributes"].get("tba", None)

    def poster_image(self,
                     _type: Optional[Literal["tiny", "small",
                                             "medium", "large", "original"]] = "original"
                     ) -> Optional[str]:
        return self._data["attributes"]["posterImage"].get(_type, None)

    def cover_image(self,
                    _type: Optional[Literal["tiny", "small",
                                            "large", "original"]] = "original"
                    ) -> Optional[str]:
        return self._data["attributes"]["coverImage"].get(_type, None)

    @property
    def episode_count(self) -> Optional[int]:
        try:
            return int(self._data["attributes"]["episodeCount"])
        except KeyError:
            return None

    @property
    def episode_length(self) -> Optional[int]:
        try:
            return int(self._data["attributes"]["episodeLength"])
        except KeyError:
            return None

    @property
    def youtube_video_id(self) -> Optional[str]:
        return self._data["attributes"].get("youtubeVideoId", None)

    @property
    def show_type(self) -> Optional[str]:
        return self._data["attributes"].get("showType", None)

    @property
    def nsfw(self) -> Optional[bool]:
        return self._data["attributes"].get("nsfw", None)
