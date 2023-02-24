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

from typing import TYPE_CHECKING, Dict, List, Literal, Optional, TypedDict

from .common import CollectionLinks, CollectionMeta, Links, MediaAttributes, Relationship, Thumbnail

if TYPE_CHECKING:
    from typing_extensions import NotRequired

__all__ = ("AnimeCollection", "AnimeData", "AnimeResource", "EpisodeData", "EpisodeResource", "EpisodeCollection")


class AnimeAttributes(MediaAttributes, TypedDict):
    subtype: Literal["ONA", "OVA", "TV", "movie", "music", "special"]
    episodeCount: int
    episodeLength: int
    youtubeVideoId: str
    nsfw: bool


class AnimeRelationships(TypedDict):
    genres: Relationship
    categories: Relationship
    castings: Relationship
    installments: Relationship
    mappings: Relationship
    reviews: Relationship
    mediaRelationships: Relationship
    characters: Relationship
    staff: Relationship
    productions: Relationship
    quotes: Relationship
    episodes: Relationship
    streamingLinks: Relationship
    animeProductions: Relationship
    animeCharacters: Relationship
    animeStaff: Relationship


class AnimeData(TypedDict):
    id: str
    type: Literal["anime"]
    links: Links
    attributes: AnimeAttributes
    relationships: AnimeRelationships


class AnimeResource(TypedDict):
    data: AnimeData
    included: NotRequired[List[EpisodeData]]


class AnimeCollection(TypedDict):
    data: List[AnimeData]
    included: NotRequired[List[EpisodeData]]
    meta: CollectionMeta
    links: CollectionLinks


class EpisodeAttributes(TypedDict):
    createdAt: str
    updatedAt: str
    synopsis: str
    titles: Dict[str, str]
    canonicalTitle: str
    seasonNumber: int
    number: int
    relativeNumber: int
    airdate: str
    length: int
    thumbnail: Optional[Thumbnail]


class EpisodeRelationships:
    media: Relationship
    videos: Relationship


class EpisodeData(TypedDict):
    id: str
    type: Literal["episodes"]
    links: Links
    attributes: EpisodeAttributes
    relationships: EpisodeRelationships


class EpisodeResource(TypedDict):
    data: EpisodeData


class EpisodeCollection(TypedDict):
    data: List[EpisodeData]
    meta: CollectionMeta
    links: CollectionLinks
