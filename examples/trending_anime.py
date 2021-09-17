import kitsu
import asyncio

client = kitsu.Client()

async def main():
    data = await client.trending_anime()

    print(f"Found [{len(data)}] trending animes")
    for anime in data:
        print("Canonical Title: " + anime.canonical_title)
        print("Average Rating: " + str(anime.average_rating))
        print("\n")
    
    # Close the internal aiohttp ClientSession
    await client.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
