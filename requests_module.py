import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def get_all_links(url):
    """
    Retrieve all hyperlinks from a specified webpage.

    This function sends an HTTP GET request to the provided URL, and then parses
    the HTML content of the page using BeautifulSoup. It extracts and returns all 
    hyperlinks ('a' tags) found in the HTML. Only valid hyperlinks (with href attribute)
    are included in the returned list.

    Args:
    url (str): The URL of the webpage from which to scrape the hyperlinks.

    Returns:
    list: A list of strings, each being a hyperlink found on the specified webpage.
          The list can be empty if no hyperlinks are found or if the page fails to load.

    Raises:
    requests.RequestException: If there is an issue with the network or the HTTP request.
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    return [link.get('href') for link in soup.find_all('a') if link.get('href')]

def fetch_and_parse(url):
    """
    Fetch the content of a webpage and parse it with BeautifulSoup.

    This function attempts to retrieve the content of the webpage at the given URL.
    If successful (HTTP status code 200), it parses the content using BeautifulSoup
    and returns the parsed object. If the request fails, it prints an error message
    and returns None. This function is useful for further HTML processing after fetching
    the webpage content.

    Args:
    url (str): The URL of the webpage to fetch and parse.

    Returns:
    BeautifulSoup object: Parsed HTML content of the webpage if successful, otherwise None.

    Raises:
    requests.RequestException: If there is an error during the HTTP request.
                               The specific exception is caught and printed to the console.
    """
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return BeautifulSoup(response.content, 'html.parser')
        else:
            print(f"Failed to fetch {url}, status code: {response.status_code}")
    except requests.RequestException as e:
        print(f"Error during request to {url}: {e}")

    return None
