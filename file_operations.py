def write_to_file(filename, content):
    """
    Write the given content to a file specified by the filename.

    This function opens a file in write mode and writes the specified content to it.
    If the file does not exist, it is created. If it does exist, its content is overwritten.
    The function uses UTF-8 encoding to support a wide range of characters.

    Parameters:
    filename (str): The path to the file where the content will be written.
                    It can be either an absolute or a relative path.
    content (str): The content to be written to the file. 

    Returns:
    None: This function does not return anything. It only performs a write operation.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content)


def read_from_file(file_path):
    """
    Read and return the content of a file specified by the file_path.

    This function opens a file in read mode and reads its entire content.
    It is assumed that the file exists and is readable. If the file does not exist,
    or if there's an error in opening the file, the function will raise an IOError.

    Parameters:
    file_path (str): The path to the file from which the content will be read.
                     It can be either an absolute or a relative path.

    Returns:
    str: The content read from the file.
    """
    with open(file_path, 'r') as file:
        return file.read()
