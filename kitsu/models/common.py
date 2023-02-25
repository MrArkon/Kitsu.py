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

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..types import Image as ImagePayload


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
