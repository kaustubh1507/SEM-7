import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time

# Set to store visited URLs to avoid duplicates
visited_urls = set()


def crawl(url, depth=1, max_depth=2):
    """
    A simple web crawler that crawls a given URL up to a specified depth.

    Parameters:
    - url: The starting URL to crawl.
    - depth: The current depth of the crawler.
    - max_depth: Maximum depth for recursion.
    """
    # Avoid crawling beyond the maximum depth
    if depth > max_depth:
        return

    # Check if the URL has already been visited
    if url in visited_urls:
        return

    print(f"Crawling: {url} (Depth: {depth})")

    try:
        # Send a GET request to the URL
        response = requests.get(url)
        # If the response status is not 200 (OK), return
        if response.status_code != 200:
            return

        # Mark the URL as visited
        visited_urls.add(url)

        # Parse the content with BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract all the anchor tags and find the href attributes (links)
        for link in soup.find_all('a', href=True):
            next_url = link['href']
            # Resolve relative URLs to absolute URLs
            next_url = urljoin(url, next_url)

            # Recursively crawl the next URLs
            crawl(next_url, depth + 1, max_depth)

    except requests.RequestException as e:
        print(f"Error crawling {url}: {e}")

    # Sleep to avoid overloading the server (politeness)
    time.sleep(1)


if __name__ == "__main__":
    # Start crawling from the base URL
    start_url = "https://example.com"
    crawl(start_url, max_depth=2)  # Crawl up to a depth of 2
