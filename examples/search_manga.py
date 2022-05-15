import kitsu
import asyncio

client = kitsu.Client()

async def main():
    # Search a specific manga with the name
    manga = await client.search_manga("Solo Leveling", limit=1)
    
    print("Canonical Title: " + manga.canonical_title)
    print("Average Rating: " + str(manga.average_rating))
    
    # This returns a list of 5 upcoming mangas
    upcoming_mangas = await client.search_manga(limit=5, status="upcoming")
    
    print(*[m.title for m in upcoming_mangas], sep=", ")
    
    # Close the internal aiohttp ClientSession
    await client.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
