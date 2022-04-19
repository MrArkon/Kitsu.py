import kitsu_extended
import asyncio

client = kitsu_extended.Client()

async def main():
    anime = await client.search_anime("jujutsu kaisen", limit=1)
    
    print("Canonical Title: " + anime.canonical_title)
    print("Average Rating: " + str(anime.average_rating))
    
    # Close the internal aiohttp ClientSession
    await client.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
