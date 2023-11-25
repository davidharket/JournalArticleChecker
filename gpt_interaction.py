import openai


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
