# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2026-08-08 08:57:58
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2026-08-08 12:06:03
"""
Get posts from external API
"""

import asyncio

from httpx import AsyncClient

BASE_URL = "https://jsonplaceholder.typicode.com/posts"


async def async_get_post(client: AsyncClient, post_id: int):
    """
    Retrieves a post from external API
    """
    url = f"{BASE_URL}/{post_id}"

    response = await client.get(url)
    response.raise_for_status()
    return response.json()


async def main():
    """
    Main function
    """
    async with AsyncClient() as client:
        tasks = [async_get_post(client, i) for i in range(1, 6)]
        posts = await asyncio.gather(*tasks)
    print(posts)


if __name__ == "__main__":
    asyncio.run(main())
