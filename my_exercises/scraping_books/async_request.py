import time
import async_timeout
import asyncio
import aiohttp


async def fetch_page(session, url):
    page_start = time.time()
    async with async_timeout.timeout(10):
        async with session.get(url) as response:
            print(f'Page took {time.time() - page_start}')
            return response.status

async def get_multiple_pages(*urls):
    tasks = []
    async with aiohttp.ClientSession() as session:
        for url in urls:
            tasks.append(fetch_page(session, url))
        grouped_tasks = asyncio.gather(*tasks)
        return await grouped_tasks

urls = ['https://google.com' for i in range(50)]
start = time.time()
asyncio.run(get_multiple_pages(*urls))
print(f'All took {time.time() - start}')
