# Kitsu.py: Python API wrapper for kitsu
[![Latest version](https://img.shields.io/pypi/v/kitsu.py.svg?style=flat&label=Latest&color=%234B78E6&logo=&logoColor=white)](https://pypi.python.org/pypi/httpie)
![PyPI - License](https://img.shields.io/pypi/l/kitsu.py)
[![CodeFactor](https://www.codefactor.io/repository/github/mrarkon/kitsu.py/badge/master)](https://www.codefactor.io/repository/github/mrarkon/kitsu.py/overview/master)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A simple async python wrapper for the [Kitsu.io](https://kitsu.io) API.

## Key Features
* Simple and modern Pythonic API using `async/await`
* Fully type checked

## Requirements

Python 3.8+
* [aiohttp](https://pypi.org/project/aiohttp/)
* [python-dateutil](https://pypi.org/project/aiohttp/)

## Installing
To install the library, run the following commands:
```shell
# Linux/MacOS
python3 -m pip install -U kitsu.py

# Windows
py -3 -m pip install -U kitsu.py
```

## Getting started

Search for an anime:
```python
import kitsu
import asyncio

client = kitsu.Client()

async def main():
    anime = await client.search_anime("jujutsu kaisen", limit=1)
    
    print("Canonical Title: " + anime.canonical_title)
    print("Average Rating: " + str(anime.average_rating))
    
    # Close the internal aiohttp ClientSession
    await client.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
```
This prints:
```
Canonical Title: Jujutsu Kaisen
Average Rating: 85.98
```
You can find more examples in the [examples](https://github.com/MrArkon/kitsu.py/tree/master/examples/) directory.

## License

This project is distributed under the [MIT](https://github.com/MrArkon/kitsu.py/blob/master/LICENSE.txt) license.
