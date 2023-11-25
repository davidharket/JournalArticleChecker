def write_to_file(filename, content):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content)

def read_from_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()
