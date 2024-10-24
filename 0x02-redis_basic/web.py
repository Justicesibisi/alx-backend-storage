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

@track_url_access
def get_page(url: str) -> str:
    '''Fetches the content of a web page and caches it for 10 seconds.'''
    # Check if the page content is already cached
    cached_page = r.get(f"cached:{url}")
    if cached_page:
        return cached_page.decode('utf-8')

    # If not cached, fetch the page using requests
    response = requests.get(url)
    page_content = response.text

    # Cache the page content for 10 seconds
    r.setex(f"cached:{url}", 10, page_content)
    
    return page_content

if __name__ == "__main__":
    url = "http://slowwly.robertomurray.co.uk"
    print(get_page(url))
    print(get_page(url))  # Should retrieve from cache if within 10 seconds

