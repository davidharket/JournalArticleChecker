import requests_module
import file_operations
import gpt_interaction

# URL to scrape
url_to_scrape = "http://example.com"
# File to store scraped content
scraped_content_file = "scraped_content.txt"
# OpenAI API Key
openai_api_key = "open_ai_api_key"

# Collect text from the URL
all_text_content = ""
links = requests_module.get_all_links(url_to_scrape)
for link in links:
    full_link = urljoin(url_to_scrape, link)
    soup = requests_module.fetch_and_parse(full_link)
    if soup:
        text_content = soup.get_text(separator='\n', strip=True)
        all_text_content += f"URL: {full_link}\n\n{text_content}\n\n"

file_operations.write_to_file(scraped_content_file, all_text_content)

# Read additional context
additional_context = file_operations.read_from_file(scraped_content_file)

# Define the question for GPT
question = "Which of these articles are most related to the topic of social media and content preferences?"

# Get the answer from GPT
answer = gpt_interaction.ask_gpt(question, additional_context, openai_api_key)
print(answer)
