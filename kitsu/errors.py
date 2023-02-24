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

from aiohttp import ClientResponse

__all__ = ("HTTPException", "BadRequest", "NotFound")


class HTTPException(Exception):
    """Generic API exception when the response code is a not 2xx.

    Attributes
    ----------
    response: :class:`~aiohttp.ClientResponse`
        The raw response object from the request.
    message: :class:`str`
        The error message sent by the API.
    status: :class:`int`
        The HTTP status code of the response.
    """

    def __init__(self, response: ClientResponse, message: str, status: int) -> None:
        self.response: ClientResponse = response
        self.message: str = message
        self.status: int = status

        super().__init__(f"{self.status} {self.message}")


class BadRequest(HTTPException):
    """Raised when the API query is malformed.

    Attributes
    ----------
    response: :class:`~aiohttp.ClientResponse`
        The raw response object from the request.
    message: :class:`str`
        The error message sent by the API.
    status: Literal[400]
        The HTTP status code of the response.
    """

    def __init__(self, response: ClientResponse, message: str) -> None:
        self.response: ClientResponse = response
        self.message: str = message

        super().__init__(response, message, 400)


class NotFound(HTTPException):
    """Raised when the requested API item was not found.

    Attributes
    ----------
    response: :class:`~aiohttp.ClientResponse`
        The raw response object from the request.
    message: :class:`str`
        The error message sent by the API.
    status: Literal[404]
        The HTTP status code of the response.
    """

    def __init__(self, response: ClientResponse, message: str) -> None:
        self.response: ClientResponse = response
        self.message: str = message

        super().__init__(response, message, 404)
