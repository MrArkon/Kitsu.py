<h1 align="center">Kitsu.py</h1>

<div align="center">
  <strong>Python API wrapper for kitsu.io</strong>
</div>
<div align="center">
  A Simple & Lightweight Asynchronous Python Wrapper for Kitsu’s Manga & Anime API.
</div>

<br />


<div align="center">
  <!-- License -->
  <a href="https://github.com/MrArkon/kitsu.py/blob/master/LICENSE">
    <img src="https://img.shields.io/pypi/l/kitsu.py?label=License&style=flat-square"
      alt="License" />
  </a>
  <!-- Code Quality -->
  <a href="https://www.codacy.com/gh/MrArkon/Kitsu.py/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=MrArkon/Kitsu.py&amp;utm_campaign=Badge_Grad">
    <img src="https://img.shields.io/codacy/grade/a04e4a4edbb84f6ea6d0c5a091a912a5?label=Code%20Quality&style=flat-square" />
  </a>
  <!-- Downloads -->
   <img src="https://img.shields.io/pypi/dm/Kitsu.py?label=Downloads&style=flat-square" />
  <!-- PyPi Version -->
  <a href="https://pypi.python.org/pypi/kitsu.py">
      <img src="https://img.shields.io/pypi/v/Kitsu.py?label=PyPi&style=flat-square" />
  </a>
  <!-- PyPi Version -->
  <img src="https://img.shields.io/pypi/pyversions/Kitsu.py?label=Python&style=flat-square" />
</div>

<div align="center">
  <h3>
    <a href="https://kitsu-py.readthedocs.io/">
      Documentation
    </a>
    <span> | </span>
    <a href="https://pypi.org/project/Kitsu.py/">
      Project Page
    </a>
    <span> | </span>
    <a href="https://github.com/MrArkon/Kitsu.py/blob/master/CHANGELOG.md">
        Changelog
    </a>
  </h3>
</div>


## Features
* **Simple and Modern** — Simple and Modern Pythonic API using `async/await`.
* **Typed** — Fully typed to provide a smooth experience while programming.
* **Features** — Get information about Categories, Episodes, Streaming Links and a lot more!
* **Custom Search** — Find any Anime/Manga using Filters or Trending Animes & Mangas.

## Requirements

Python 3.8+
* [aiohttp](https://pypi.org/project/aiohttp/)
* [python-dateutil](https://pypi.org/project/python-dateutil)

## Installing
To install the library, run the following commands:
```shell
# Linux/MacOS
python3 -m pip install -U kitsu.py

# Windows
py -3 -m pip install -U kitsu.py
```

## Example

Search for an anime:
```python
import kitsu
import asyncio

client = kitsu.Client()

async def main():
    # Search a specific anime with the name
    anime = await client.search_anime("jujutsu kaisen", limit=1)
    
    print("Canonical Title: " + anime.canonical_title)
    print("Average Rating: " + str(anime.average_rating))
    
    # This returns a list of 5 animes in the spring season 2022
    animes_in_spring = await client.search_anime(limit=5, season_year=2022, season='spring')
    
    print(*[a.title for a in animes_in_spring], sep=", ")
    
    # Close the internal aiohttp ClientSession
    await client.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
```
This prints:
```
Canonical Title: Jujutsu Kaisen
Average Rating: 85.98
That Time I Got Reincarnated as a Slime: Ramiris to the Rescue, Blue Thermal, Q&A=E, Smol Adventures, Estab-Life: Great Escape
```
You can find more examples in the [examples](https://github.com/MrArkon/kitsu.py/tree/master/examples/) directory.

## License

This project is distributed under the [MIT](https://github.com/MrArkon/kitsu.py/blob/master/LICENSE.txt) license.
