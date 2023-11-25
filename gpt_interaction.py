from openai import OpenAI


# Function to ask GPT a question
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
    # Combine the scraped content with additional context
    prompt = f"{additional_context}\\n\\n{question}"

    # Query GPT and return the response | Keep in mind, API key must be passed via Authorization HTTP header (e.g., Authorization: Bearer OPENAI_API_KEY)
    client = OpenAI()
    
    response = client.chat.completions.create(
      model="gpt-3.5-turbo-16k",
      messages=[
        {
          "role": "system",
          "content": "You compare html data from databases on journal articles. The user will ask you a question, and you will use  the data provided from the HTML to assess it."
        },
        {
          "role": "user",
          "content": prompt
        }
      ]
    )
    return response.choices[0].text.strip()
