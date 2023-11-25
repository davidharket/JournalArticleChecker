import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import openai

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

def collect_text_to_file(url, filename):
    """
    Scrape and collect text from all links found at the given URL and save it to a file.

    Args:
    url (str): The URL from which to scrape text.
    filename (str): The filename where the scraped text will be saved.

    Returns:
    None
    """
    links = get_all_links(url)
    all_text_content = ""

    for link in links:
        full_link = urljoin(url, link)
        print(f"Collecting text from {full_link}")

        try:
            response = requests.get(full_link)
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                text_content = soup.get_text(separator='\n', strip=True)
                all_text_content += f"URL: {full_link}\n\n{text_content}\n\n"
                print(f"Collected text from {full_link}")
            else:
                print(f"Failed to collect from {full_link}, status code: {response.status_code}")
        except requests.RequestException as e:
            print(f"Error during request to {full_link}: {e}")

    with open(filename, 'w', encoding='utf-8') as file:
        file.write(all_text_content)

def read_additional_context(file_path):
    """
    Read and return the content of the specified file.

    Args:
    file_path (str): The path to the file containing additional context.

    Returns:
    str: The content of the file.
    """
    with open(file_path, 'r') as file:
        return file.read()

def ask_gpt(question, additional_context, openai_api_key):
    """
    Query the OpenAI GPT model with a specific question and additional context.

    Args:
    question (str): The question to be asked to the GPT model.
    additional_context (str): Additional context to provide to the GPT model.
    openai_api_key (str): The API key for OpenAI.

    Returns:
    str: The answer from the GPT model.
    """
    openai.api_key = openai_api_key

    prompt = f"{additional_context}\\n\\n{question}"

    response = openai.Completion.create(
        engine="gpt-3.5-turbo",
        prompt=prompt,
        max_tokens=50000
    )
    return response.choices[0].text.strip()

if __name__ == "__main__":
    # URL to scrape
    url_to_scrape = "http://example.com"
    # File to store scraped content
    scraped_content_file = "scraped_content.txt"
    # File with additional context
    additional_context_file = scraped_content_file
    # OpenAI API Key
    openai_api_key = "open_ai_api_key"

    # Collect text from the URL
    collect_text_to_file(url_to_scrape, scraped_content_file)

    # Read additional context
    additional_context = read_additional_context(additional_context_file)

    # Define the question for GPT
    question = "Which of these articles are most related to the topic of social media and content preferences?"

    # Get the answer from GPT
    answer = ask_gpt(question, additional_context, openai_api_key)
    print(answer)
