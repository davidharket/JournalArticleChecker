import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def get_all_links(url):
    # ... existing code for get_all_links ...

def fetch_and_parse(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return BeautifulSoup(response.content, 'html.parser')
        else:
            print(f"Failed to fetch {url}, status code: {response.status_code}")
    except requests.RequestException as e:
        print(f"Error during request to {url}: {e}")
    return None
