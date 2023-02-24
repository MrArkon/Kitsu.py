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

if TYPE_CHECKING:
    from typing_extensions import NotRequired


class MediaAttributes(TypedDict):
    createdAt: str
    updatedAt: str
    slug: str
    synopsis: str
    titles: Dict[str, str]
    canonicalTitle: str
    abbreviatedTitles: List[str]
    averageRating: Optional[str]
    ratingFrequencies: Dict[str, str]
    userCount: int
    favoritesCount: int
    startDate: str
    endDate: Optional[str]
    popularityRank: int
    ratingRank: int
    ageRating: Literal["G", "PG", "R", "R18"]
    ageRatingGuide: str
    posterImage: Optional[Image]
    coverImage: Optional[Image]
    status: Literal["current", "finished", "tba", "unreleased", "upcoming"]


class Thumbnail(TypedDict):
    original: str


class ImageDimension(TypedDict):
    width: Optional[str]
    height: Optional[str]


class ImageDimensions(TypedDict):
    tiny: ImageDimension
    small: ImageDimension
    medium: ImageDimension
    large: ImageDimension


class ImageMeta(TypedDict):
    dimensions: ImageDimensions


class Image(TypedDict):
    tiny: str
    small: str
    medium: str
    large: str
    original: str
    meta: ImageMeta


class Links(TypedDict, total=False):
    self: str
    related: str


class Relationship(TypedDict):
    links: Links


class CollectionMeta(TypedDict):
    count: int


class CollectionLinks(TypedDict):
    first: str
    prev: NotRequired[str]
    next: NotRequired[str]
    last: str
