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

from enum import Enum

__all__ = ("AgeRating", "Status", "Season", "AnimeSubtype", "MangaSubtype")


class AgeRating(Enum):
    G = "G"
    PG = "PG"
    R = "R"
    R18 = "R18"

    def __str__(self) -> str:
        return self.value


class Status(Enum):
    current = "current"
    finished = "finished"
    tba = "tba"
    unreleased = "unreleased"
    upcoming = "upcoming"

    def __str__(self) -> str:
        return self.value


class Season(Enum):
    spring = "spring"
    summer = "summer"
    fall = "fall"
    winter = "winter"

    def __str__(self) -> str:
        return self.value


class AnimeSubtype(Enum):
    ONA = "ONA"
    OVA = "OVA"
    TV = "TV"
    movie = "movie"
    music = "music"
    special = "special"

    def __str__(self) -> str:
        return self.value


class MangaSubtype(Enum):
    doujin = "doujin"
    manga = "manga"
    manhua = "manhua"
    manhwa = "manhwa"
    novel = "novel"
    oel = "oel"
    oneshot = "oneshot"

    def __str__(self) -> str:
        return self.value
