import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def get_all_links(url):
    """
    Retrieve all hyperlinks from the specified URL.
    Args:
    url (str): The URL from which to scrape the hyperlinks.
    Returns:
    list: A list of hyperlinks found on the specified webpage.
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    return [link.get('href') for link in soup.find_all('a') if link.get('href')]

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
