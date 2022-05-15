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
