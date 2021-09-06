"""
Kitsu.io API Wrapper
~~~~~~~~~~~~~~~~~~~
A simple async wrapper for the Kitsu.io API.
:copyright: (c) 2021-present MrArkon
:license: MIT, see LICENSE.txt for more details.

"""

__title__ = "kitsu"
__version__ = "0.1.0a0"
__author__ = "MrArkon"
__license__ = 'MIT'
__copyright__ = 'Copyright 2021-present MrArkon'

__path__ = __import__('pkgutil').extend_path(__path__, __name__)

from .client import *
from .errors import *
from .models import *
