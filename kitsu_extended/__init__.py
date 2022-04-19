"""
Kitsu.io API Wrapper
~~~~~~~~~~~~~~~~~~~
A simple async python wrapper for the Kitsu.io API.
:copyright: (c) 2021-2022 MrArkon, 2022-present Dymattic
:license: MIT, see LICENSE.txt for more details.

"""

__title__   = "kitsu_extended"
__version__ = "1.0.4"
__author__  = "Dymattic"
__license__ = 'MIT'
__copyright__ = 'Copyright 2021-2022 MrArkon, 2022-present Dymattic'

__all__  = ('Client', 'HTTPException', 'BadRequest', 'NotFound', 'Anime', 'Manga')
__path__ = __import__('pkgutil').extend_path(__path__, __name__)

from logging import NullHandler, getLogger

from .client import Client
from .errors import BadRequest, HTTPException, NotFound
from .models import Anime, Manga

getLogger(__name__).addHandler(NullHandler())
