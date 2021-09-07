"""
MIT License

Copyright (c) 2021 MrArkon

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

from typing import Any, Optional, Union

__all__ = ("KitsuError", "HTTPException")


class KitsuError(Exception):
    """
    The base error
    """

    def __init__(self, message: Optional[str], *args: Any, **kwargs: Any) -> None:
        super().__init__(message, *args, **kwargs)


class HTTPException(Exception):

    def __init__(self,
                 title: Optional[str],
                 detail: Optional[str],
                 code: Optional[Union[str, int]],
                 *args: Any,
                 **kwargs: Any
                 ) -> None:
        super().__init__(title, detail, code, *args, **kwargs)

        self.title: Optional[str] = title
        self.detail: Optional[str] = detail
        self.code: Optional[Union[str, int]] = code


class ServerTimeout(KitsuError):
    pass
