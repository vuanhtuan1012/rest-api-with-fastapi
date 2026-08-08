# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2026-08-08 09:22:34
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2026-08-08 10:03:19
"""
Get posts from external API
"""

import requests

BASE_URL = "https://jsonplaceholder.typicode.com/posts"


class PostService:  # pylint:disable=R0903
    """
    PostService class
    """

    def __init__(self, repository: dict[int, dict]) -> None:
        self.repository = repository

    def get_post_by_id(self, post_id: int) -> dict:
        """
        Retrieves post from database
        """
        return self.repository.get(post_id, {})


def get_post(post_id: int):
    """
    Retrieves a post from external API
    """
    url = f"{BASE_URL}/{post_id}"
    response = requests.get(url, timeout=5)
    return response.json()


def main():
    """
    Main function
    """
    # retrieves post from database
    repository = {
        1: {
            "userId": 1,
            "id": 1,
            "title": "first post title",
            "body": "first post body",
        },
        2: {
            "userId": 1,
            "id": 2,
            "title": "second post title",
            "body": "second post body",
        },
    }
    post_service = PostService(repository)
    post = post_service.get_post_by_id(1)
    print(post)

    # retrieves post from API
    post = get_post(1)
    print(post)


if __name__ == "__main__":
    main()
