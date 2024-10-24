#!/usr/bin/env python3
'''A module for fetching and caching web pages with access tracking.
'''
import redis
import requests
from functools import wraps

# Connect to Redis
r = redis.Redis()

def track_url_access(method):
    '''Decorator to track the number of times a URL is accessed.'''
    @wraps(method)
    def wrapper(url: str, *args, **kwargs) -> str:
        count_key = f"count:{url}"
        # Increment the access count in Redis
        r.incr(count_key)
        return method(url, *args, **kwargs)
    return wrapper

def cache_page(method):
    '''Decorator to cache the page content for 10 seconds.'''
    @wraps(method)
    def wrapper(url: str, *args, **kwargs) -> str:
        cache_key = f"cached:{url}"
        # Check if the page content is already cached
        cached_page = r.get(cache_key)
        if cached_page:
            # Return cached content if available
            return cached_page.decode('utf-8')

        # Otherwise, fetch the page content
        page_content = method(url, *args, **kwargs)
        
        # Cache the content for 10 seconds
        r.setex(cache_key, 10, page_content)
        return page_content
    return wrapper

@track_url_access
@cache_page
def get_page(url: str) -> str:
    '''Fetches the content of a web page.'''
    response = requests.get(url)
    return response.text

if __name__ == "__main__":
    url = "http://slowwly.robertomurray.co.uk"
    print(get_page(url))  # First request, fetches and caches
    print(get_page(url))  # Second request, serves from cache if within 10 seconds

