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
from typing import TYPE_CHECKING, List, Optional

from .enums import AgeRating, AnimeSubtype, MangaSubtype, Status

if TYPE_CHECKING:
    from .client import Client
    from .types import AnimeData, EpisodeCollection, EpisodeData
    from .types import Image as ImagePayload
    from .types import MangaData

__all__ = ("Image", "Anime", "Episode", "Manga")


class Image:
    """
    Represents a poster/cover image for an Anime or Manga.

    Attributes
    ----------
    tiny: :class:`str`
        The URL of this image in its tiny size.
    small: :class:`str`
        The URL of this image in its small size.
    medium: :class:`str`
        The URL of this image in its medium size.
    large: :class:`str`
        The URL of this image in its large size.
    original: :class:`str`
        The URL of this image in its original size.
    """

    __slots__ = ("_data", "tiny", "small", "medium", "large", "original")

    def __init__(self, payload: ImagePayload) -> None:
        self._data = payload

        self.tiny = self._data["tiny"]
        self.small = self._data["small"]
        self.medium = self._data["medium"]
        self.large = self._data["large"]
        self.original = self._data["original"]


class Episode:
    """Represents an Episode returned from the Kitsu API.

    Attributes
    ----------
    id: :class:`int`
        The UUID associated with the Episode on Kitsu.
    synopsis: :class:`str`
        The synopsis/description of this Episode.
    description: :class:`str`
        Alias to synopsis.
    canonical_title: :class:`str`
        The canonical title of this Episode.
    season_number: :class:`int`
        The season number in which this Episode appears.
    number: :class:`int`
        The Episode number.
    relative_number: :class:`int`
        The relative Episode number.
    length: :class:`int`
        The length of this Episode in minutes.
    """

    __slots__ = (
        "_data",
        "_attributes",
        "id",
        "synopsis",
        "description",
        "_titles",
        "canonical_title",
        "season_number",
        "number",
        "relative_number",
        "length",
    )

    def __init__(self, payload: EpisodeData) -> None:
        self._data = payload
        self._attributes = payload["attributes"]

        self.id = int(self._data["id"])
        self.synopsis = self._attributes["synopsis"]
        self.description = self.synopsis
        self._titles = self._attributes["titles"]
        self.canonical_title = self._attributes["canonicalTitle"]
        self.season_number = self._attributes["seasonNumber"]
        self.number = self._attributes["number"]
        self.relative_number = self._attributes["relativeNumber"]
        self.length = self._attributes["length"]

    def __repr__(self) -> str:
        return f"<kitsu.Episode id={self.id} title={self.title}>"

    def __str__(self) -> str:
        return self.title

    @property
    def title(self) -> str:
        """The title of the Episode, defaults to ``en`` language key in the
        titles mapping, fall backs to the next available key if the ``en``
        key is not present.
        """
        return self._titles.get("en", (list(self._titles.values())[0]))

    @property
    def created_at(self) -> datetime:
        """The UTC datetime of when this Episode was created."""
        return datetime.strptime(self._attributes["createdAt"], "%Y-%m-%dT%H:%M:%S.%fZ")

    @property
    def updated_at(self) -> Optional[datetime]:
        """The UTC datetime of when this Episode was last updated."""
        return datetime.strptime(self._attributes["updatedAt"], "%Y-%m-%dT%H:%M:%S.%fZ")

    @property
    def airdate(self) -> datetime:
        """The UTC datetime of when this Episode aired."""
        return datetime.strptime(self._attributes["airdate"], "%Y-%m-%d")

    @property
    def thumbnail(self) -> Optional[str]:
        """The URL to the thumbnail of this Episode."""
        if (thumbnail := self._attributes["thumbnail"]) is not None:
            return thumbnail["original"]


class Anime:
    """Represents an Anime returned from the Kitsu API.

    Attributes
    ----------
    id: :class:`int`
        The UUID associated with this Anime on Kitsu.
    slug: :class:`str`
        The unique string identifier for this Anime.
    synopsis: :class:`str`
        The synopsis/description of this Anime.
    description: :class:`str`
        Alias to synopsis.
    canonical_title: :class:`str`
        The canonical title of this Anime.
    abbreviated_titles: List[:class:`str`]
        A list of abbreviated titles for this Anime.
    average_rating: Optional[:class:`float`]
        The average rating of this Anime out of 100 on Kitsu.
    rating_frequencies: Dict[:class:`str`, :class:`str`]
        A mapping of ratings to its frequencies for this Anime.
    user_count: :class:`int`
        The number of users associated with this Anime on Kitsu.
    favorites_count: :class:`int`
        The number of users who have added this Anime to their favorites.
    popularity_rank: :class:`int`
        The popularity rank of this Anime on Kitsu.
    rating_rank: :class:`int`
        The rating rank of this Anime on Kitsu.
    age_rating: :class:`AgeRating`
        The age rating of this Anime.
    age_rating_guide: :class:`str`
        A string describing the age rating of this Anime.
    subtype: :class:`AnimeSubtype`
        The subtype of this Anime.
    status: :class:`Status`
        The status of this Anime.
    episode_count: :class:`int`
        The number of episodes in this Anime.
    episode_length: :class:`int`
        The average length of each episode in minutes.
    youtube_video_id: :class:`str`
        The youtube video id associated with this Anime.
    nsfw: :class:`bool`
        Whether this Anime is marked as NSFW.
    """

    __slots__ = (
        "_data",
        "_attributes",
        "_client",
        "_included",
        "id",
        "slug",
        "synopsis",
        "description",
        "_titles",
        "canonical_title",
        "abbreviated_titles",
        "average_rating",
        "rating_frequencies",
        "user_count",
        "favorites_count",
        "popularity_rank",
        "rating_rank",
        "age_rating",
        "age_rating_guide",
        "subtype",
        "status",
        "episode_count",
        "episode_length",
        "youtube_video_id",
        "nsfw",
        "__episodes",
    )

    def __init__(self, payload: AnimeData, client: Client, *, included: Optional[List[EpisodeData]] = None) -> None:
        self._data = payload
        self._attributes = self._data["attributes"]
        self._client = client
        self._included = included

        self.id = int(self._data["id"])
        self.slug = self._attributes["slug"]
        self.synopsis = self._attributes["synopsis"]
        self.description = self.synopsis
        self._titles = self._attributes["titles"]
        self.canonical_title = self._attributes["canonicalTitle"]
        self.abbreviated_titles = self._attributes["abbreviatedTitles"]
        self.average_rating = None if self._attributes["averageRating"] is None else float(self._attributes["averageRating"])
        self.rating_frequencies = self._attributes["ratingFrequencies"]
        self.user_count = self._attributes["userCount"]
        self.favorites_count = self._attributes["favoritesCount"]
        self.popularity_rank = self._attributes["popularityRank"]
        self.rating_rank = self._attributes["ratingRank"]
        self.age_rating = AgeRating(self._attributes["ageRating"])
        self.age_rating_guide = self._attributes["ageRatingGuide"]
        self.subtype = AnimeSubtype(self._attributes["subtype"])
        self.status = Status(self._attributes["status"])
        self.episode_count = self._attributes["episodeCount"]
        self.episode_length = self._attributes["episodeLength"]
        self.youtube_video_id = self._attributes["youtubeVideoId"]
        self.nsfw = self._attributes["nsfw"]

        self.__episodes: Optional[List[Episode]] = None

    def __repr__(self) -> str:
        return f"<kitsu.Anime id={self.id} title={self.title}>"

    def __str__(self) -> str:
        return self.title

    @property
    def url(self) -> str:
        """The Kitsu URL to this Anime."""
        return f"https://kitsu.io/anime/{self.slug}"

    @property
    def title(self) -> str:
        """The title of the Anime, defaults to ``en`` language key in the
        titles mapping, fall backs to the next available key if the ``en``
        key is not present."""
        return self._titles.get("en", (list(self._titles.values())[0]))

    @property
    def created_at(self) -> datetime:
        """The UTC datetime of when this Anime was created."""
        return datetime.strptime(self._attributes["createdAt"], "%Y-%m-%dT%H:%M:%S.%fZ")

    @property
    def updated_at(self) -> Optional[datetime]:
        """The UTC datetime of when this Anime was last updated."""
        return datetime.strptime(self._attributes["updatedAt"], "%Y-%m-%dT%H:%M:%S.%fZ")

    @property
    def start_date(self) -> datetime:
        """The UTC datetime of when this Anime started."""
        return datetime.strptime(self._attributes["startDate"], "%Y-%m-%d")

    @property
    def end_date(self) -> Optional[datetime]:
        """The UTC datetime of when this Anime ended, if it has."""
        if (payload := self._attributes["endDate"]) is not None:
            return datetime.strptime(payload, "%Y-%m-%d")

    @property
    def poster_image(self) -> Optional[Image]:
        """The poster image of this Anime."""
        if (payload := self._attributes["posterImage"]) is not None:
            return Image(payload)

    @property
    def cover_image(self) -> Optional[Image]:
        """The cover image of this Anime."""
        if (payload := self._attributes["coverImage"]) is not None:
            return Image(payload)

    @property
    def episodes(self) -> Optional[List[Episode]]:
        """The episodes for this Anime."""

        if self.__episodes:
            if not self._included:
                return None

            episodes = [Episode(data) for data in self._included if data["type"] == "episodes"]

            if not episodes:
                return None

            self.__episodes = episodes

        return self.__episodes

    @episodes.setter
    def episodes(self, value: List[Episode]) -> None:
        self.__episodes = [item for item in value if isinstance(item, Episode)]

    async def get_episodes(self) -> Optional[List[Episode]]:
        """Fetches the episodes for this Anime and caches the response.

        Returns
        -------
        Optional[List[:class:`Episode`]]
        """
        if self.episodes is None:
            data: EpisodeCollection = await self._client._request(f"anime/{self.id}/episodes", params={"page[limit]": 20})
            episodes = [Episode(payload) for payload in data["data"]]

            next_page_url = data["links"].get("next")

            while next_page_url is not None:
                next_page: EpisodeCollection = await self._client._request(url=next_page_url)
                next_page_url = next_page["links"].get("next")

                episodes.extend(Episode(payload) for payload in next_page["data"])

            if not episodes:
                return None

            self.episodes = episodes

        return self.episodes


class Manga:
    """Represents an Manga returned from the Kitsu API.

    Attributes
    ----------
    id: :class:`int`
        The UUID associated with this Manga on Kitsu.
    slug: :class:`str`
        The unique string identifier for this Manga.
    synopsis: :class:`str`
        The synopsis/description of this Manga.
    description: :class:`str`
        Alias to synopsis.
    canonical_title: :class:`str`
        The canonical title of this Manga.
    abbreviated_titles: List[:class:`str`]
        A list of abbreviated titles for this Manga.
    average_rating: Optional[:class:`float`]
        The average rating of this Manga out of 100 on Kitsu.
    rating_frequencies: Dict[:class:`str`, :class:`str`]
        A mapping of ratings to its frequencies for this Manga.
    user_count: :class:`int`
        The number of users associated with this Manga on Kitsu.
    favorites_count: :class:`int`
        The number of users who have added this Manga to their favorites.
    popularity_rank: :class:`int`
        The popularity rank of this Manga on Kitsu.
    rating_rank: :class:`int`
        The rating rank of this Manga on Kitsu.
    age_rating: :class:`AgeRating`
        The age rating of this Manga.
    age_rating_guide: Optional[:class:`str`]
        A string describing the age rating of this Manga.
    subtype: :class:`MangaSubtype`
        The subtype of this Manga.
    status: :class:`Status`
        The status of this Manga.
    chapter_count: :class:`int`
        The number of chapters in the Manga.
    volume_count: :class:`int`
        The number of volumes of this Manga.
    serialization: :class:`str`
        The supporter/publisher of this Manga.
    """

    __slots__ = (
        "_data",
        "_attributes",
        "_client",
        "id",
        "slug",
        "synopsis",
        "description",
        "_titles",
        "canonical_title",
        "abbreviated_titles",
        "average_rating",
        "rating_frequencies",
        "user_count",
        "favorites_count",
        "popularity_rank",
        "rating_rank",
        "age_rating",
        "age_rating_guide",
        "subtype",
        "status",
        "chapter_count",
        "volume_count",
        "serialization",
    )

    def __init__(self, payload: MangaData, client: Client) -> None:
        self._data = payload
        self._attributes = self._data["attributes"]
        self._client = client

        self.id = int(self._data["id"])
        self.slug = self._attributes["slug"]
        self.synopsis = self._attributes["synopsis"]
        self.description = self.synopsis
        self._titles = self._attributes["titles"]
        self.canonical_title = self._attributes["canonicalTitle"]
        self.abbreviated_titles = self._attributes["abbreviatedTitles"]
        self.average_rating = None if self._attributes["averageRating"] is None else float(self._attributes["averageRating"])
        self.rating_frequencies = self._attributes["ratingFrequencies"]
        self.user_count = self._attributes["userCount"]
        self.favorites_count = self._attributes["favoritesCount"]
        self.popularity_rank = self._attributes["popularityRank"]
        self.rating_rank = self._attributes["ratingRank"]
        self.age_rating = AgeRating(self._attributes["ageRating"])
        self.age_rating_guide = self._attributes["ageRatingGuide"]
        self.subtype = MangaSubtype(self._attributes["subtype"])
        self.status = Status(self._attributes["status"])
        self.chapter_count = self._attributes["chapterCount"]
        self.volume_count = self._attributes["volumeCount"]
        self.serialization = self._attributes["serialization"]

    def __repr__(self) -> str:
        return f"<kitsu.Manga id={self.id} title={self.title}>"

    def __str__(self) -> str:
        return self.title

    @property
    def url(self) -> str:
        """The Kitsu URL to this Manga."""
        return f"https://kitsu.io/manga/{self.slug}"

    @property
    def title(self) -> str:
        """The title of the Manga, defaults to ``en`` language key in the
        titles mapping, fall backs to the next available key if the ``en``
        key is not present.
        """
        return self._titles.get("en", (list(self._titles.values())[0]))

    @property
    def created_at(self) -> datetime:
        """The UTC datetime of when this Manga was created."""
        return datetime.strptime(self._attributes["createdAt"], "%Y-%m-%dT%H:%M:%S.%fZ")

    @property
    def updated_at(self) -> Optional[datetime]:
        """The UTC datetime of when this Manga was last updated."""
        return datetime.strptime(self._attributes["updatedAt"], "%Y-%m-%dT%H:%M:%S.%fZ")

    @property
    def start_date(self) -> datetime:
        """The UTC datetime of when this Manga started."""
        return datetime.strptime(self._attributes["startDate"], "%Y-%m-%d")

    @property
    def end_date(self) -> Optional[datetime]:
        """The UTC datetime of when this Manga ended, if it has"""
        if (payload := self._attributes["endDate"]) is not None:
            return datetime.strptime(payload, "%Y-%m-%d")

    @property
    def poster_image(self) -> Optional[Image]:
        """The poster image of this Manga."""
        if (payload := self._attributes["posterImage"]) is not None:
            return Image(payload)

    @property
    def cover_image(self) -> Optional[Image]:
        """The cover image of this Manga."""
        if (payload := self._attributes["coverImage"]) is not None:
            return Image(payload)
