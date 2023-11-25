import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import openai


def get_all_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    return [link.get('href') for link in soup.find_all('a') if link.get('href')]


def collect_text_to_file(url, filename):
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

    # Writing to file
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(all_text_content)


# Function to read additional context from a .txt file
def read_additional_context(file_path):
    with open(file_path, 'r') as file:
        return file.read()


# Function to ask GPT a question
def ask_gpt(question, additional_context, openai_api_key):
    openai.api_key = openai_api_key

    # Combine the scraped content with additional context
    prompt = f"{additional_context}\\n\\n{question}"

    # Query GPT and return the response
    response = openai.Completion.create(
        engine="gpt-3.5-turbo",
        prompt=prompt,
        max_tokens=50000
    )
    return response.choices[0].text.strip()


# Example usage
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
