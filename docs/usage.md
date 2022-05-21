# Recipes & Examples

These are a few common examples to use with Kitsu.py, 
Please refer to [Github Examples](https://github.com/MrArkon/Kitsu.py/tree/master/examples)
for more detailed examples.

## Searching for an Anime/Manga
````{tab} Anime
```python
import kitsu
import asyncio

client = kitsu.Client()

async def main():
    # Search a specific anime with the name
    anime = await client.search_anime("jujutsu kaisen")

    # Prints the Japanese title in English characters
    print("Title [English]: " + anime.title.en_jp)

    # Prints the Japanese title in Japanese characters
    print("Title [Japanese]: " + anime.title.ja_jp)
    print("Average Rating: " + str(anime.average_rating) + "/100")

    # Make sure to await anime.categories as we have to fetch it from a different endpoint
    print("Categories: " + ", ".join(c.title for c in await anime.categories))
 
    # Close the internal aiohttp ClientSession
    await client.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
```

This outputs:
```console
Title [English]: Jujutsu Kaisen
Title [Japanese]: 呪術廻戦
Average Rating: 86.15/100 
Categories: Action, Demon, Supernatural, Fantasy, Shounen, Violence, School Life, Swordplay, Angst
```
````

````{tab} Manga
```python
import kitsu
import asyncio

client = kitsu.Client()

async def main():
    # Search a specific manga with the name
    manga = await client.search_manga("Shingeki No Kyojin")
    
    # Prints the English title
    print("Title [English]: " + manga.title.en)

    # Prints the Japanese title
    print("Title [Japanese]: " + manga.title.ja_jp)
    print("Average Rating: " + str(manga.average_rating) + "/100")

    # Make sure to await anime.categories as we have to fetch it from a different endpoint
    print("Categories: " + ", ".join(c.title for c in await manga.categories))

    # Close the internal aiohttp ClientSession
    await client.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
```

This outputs:
```console
Title [English]: Attack on Titan
Title [Japanese]: 進撃の巨人
Average Rating: 84.53/100   
Categories: Super Power, Horror, Drama, Action, Fantasy, Mystery, Shounen
``` 
````