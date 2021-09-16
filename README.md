<div align="center">
  <h1>Kitsu.py</h1>
  <a href="https://github.com/MrArkon/kitsu.py/graphs/contributors">
    <img src="https://img.shields.io/github/contributors/MrArkon/kitsu.py.svg?style=for-the-badge" />
  </a>
  <a href="https://github.com/MrArkon/kitsu.py/network/members">
    <img src="https://img.shields.io/github/forks/MrArkon/kitsu.py.svg?style=for-the-badge" />
  </a>
  <a href="https://github.com/MrArkon/kitsu.py/stargazers">
    <img src="https://img.shields.io/github/stars/MrArkon/kitsu.py.svg?style=for-the-badge" />
  </a>
  <a href="https://github.com/MrArkon/kitsu.py/issues">
    <img src="https://img.shields.io/github/issues/MrArkon/kitsu.py.svg?style=for-the-badge" />
  </a>
  <a href="https://github.com/MrArkon/kitsu.py/blob/master/LICENSE.txt">
    <img src="https://img.shields.io/github/license/MrArkon/kitsu.py.svg?style=for-the-badge" />
  </a>
  </div>
  <p align="center">
    A simple & lightweight JSON client for the <a href="https://kitsu.io/">Kitsu.io</a> API
    <br />
    <br />
    <a href="https://pypi.org/project/kitsu.py/">PyPi</a>
    ·
    <a href="https://github.com/MrArkon/kitsu.py/issues">Report Bugs</a>
    ·
    <a href="https://github.com/MrArkon/kitsu.py/issues">Request Feature</a>
  </p>
</p>

## Key Features
* Modern Pythonic API using `async` and `await`
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
    data = await client.search_anime("jujutsu kaisen", limit=1)
    
    print("Canonical Title: " + data.canonical_title)
    
    # Close the internal aiohttp ClientSession
    await client.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
```
This prints:
```
Canonical Title: Jujutsu Kaisen
```

## License

This project is distributed under the [MIT](https://github.com/MrArkon/kitsu.py/blob/master/LICENSE.txt) license.
