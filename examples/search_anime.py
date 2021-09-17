import kitsu
import asyncio

client = kitsu.Client()

async def main():
    data = await client.search_anime("jujutsu kaisen", limit=1)
    
    print("Canonical Title: " + data.canonical_title)
    print("Average Rating: " + str(data.average_rating))
    
    # Close the internal aiohttp ClientSession
    await client.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
