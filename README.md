# JournalArticleChecker
A Python script that collects the names of all journal articles from a specified journal volume page on Springer Link (e.g., https://link.springer.com/journal/42001/volumes-and-issues) and passes it to the OpenAI API to check if any literature is associated with a pre-defined context.

This script was created for the purpose of checking large online databases for semantic content. If context length is too long for specified gpt-3.5-turbo model, the .txt file created by the script can be uploaded to and assessed by a gpt 4.0-turbo model via the ChatGPT interface.
