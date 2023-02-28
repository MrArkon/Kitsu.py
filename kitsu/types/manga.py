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
from typing import Dict, List, Literal, Optional, TypedDict

from .common import CollectionLinks, CollectionMeta, Links, MediaAttributes, Relationship, Thumbnail

__all__ = ("MangaCollection", "MangaData", "MangaResource", "ChapterCollection", "ChapterData", "ChapterResource")


class MangaAttributes(MediaAttributes, TypedDict):
    subtype: Literal["doujin", "manga", "manhua", "manhwa", "novel", "oel", "oneshot"]
    chapterCount: int
    volumeCount: int
    serialization: str


class MangaRelationships(TypedDict):
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
    chapters: Relationship
    mangaCharacters: Relationship
    mangaStaff: Relationship


class MangaData(TypedDict):
    id: str
    type: Literal["manga"]
    links: Links
    attributes: MangaAttributes
    relationships: MangaRelationships


class MangaResource(TypedDict):
    data: MangaData


class MangaCollection(TypedDict):
    data: List[MangaData]
    meta: CollectionMeta
    links: CollectionLinks


class ChapterAttributes(TypedDict):
    createdAt: str
    updatedAt: str
    synopsis: str
    titles: Dict[str, str]
    canonicalTitle: Optional[str]
    volumeNumber: int
    number: int
    published: Optional[str]
    length: Optional[int]
    thumbnail: Optional[Thumbnail]


class ChapterRelationships(TypedDict):
    manga: Relationship


class ChapterData(TypedDict):
    id: str
    type: Literal["chapters"]
    links: Links
    attributes: ChapterAttributes
    relationships: ChapterRelationships


class ChapterResource(TypedDict):
    data: ChapterData


class ChapterCollection(TypedDict):
    data: List[ChapterData]
    meta: CollectionMeta
    links: CollectionLinks
