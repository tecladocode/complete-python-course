import aiohttp
import asyncio
import time

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
async def fetch_page(url):
    page_start = time.time()
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            print(f'Page took {time.time() - page_start}')


async def main():
    tasks = [fetch_page('https://google.com') for i in range(50)]
    await asyncio.gather(*tasks)


start_time = time.time()
asyncio.run(main())
print(f'All took {time.time() - start_time}')