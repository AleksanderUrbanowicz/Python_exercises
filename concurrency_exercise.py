import requests
import threading
import concurrent.futures
import requests_exercise
import time
import asyncio
import aiohttp


# Synchronous version
def get_site_content_sync(url, session):
    with session.get(url) as response:
        print(f'Content len: {len(response.content)} from {url}')


def get_all_sites_content_sync(sites):
    with requests.Session() as session:
        for url in sites:
            get_site_content_sync(url, session)


# Threading version
thread_local = threading.local()


def get_session_threading():
    if not hasattr(thread_local, 'session'):
        thread_local.session = requests.Session()
    return thread_local.session


def get_site_content_threading(url):
    session = get_session_threading()
    with session.get(url) as response:
        print(f'Content len: {len(response.content)} from {url}')


def get_all_sites_content_threading(sites):
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as pool_executor:
        pool_executor.map(get_site_content_threading, sites)


# Asyncio version
async def get_site_content_asyncio(url, session):
    async with session.get(url) as response:
        print(f'Content len: {response.content_length} from {url}')


async def get_all_sites_content_asyncio(sites):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in sites:
            tasks.append(asyncio.ensure_future(get_site_content_asyncio(url, session)))
        await asyncio.gather(*tasks)

if __name__ == '__main__':
    urls = requests_exercise.urls * 100
    start_time = time.time()
    # get_all_sites_content_sync(urls)
    # get_all_sites_content_threading(urls)
    asyncio.get_event_loop().run_until_complete(get_all_sites_content_asyncio(urls))
    time_delta = time.time() - start_time
    print(f'Downloaded {len(urls)} websites in: {time_delta}')
