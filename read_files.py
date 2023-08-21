import os
from insert_data import *

#these two lines need to delete
file_path = 'C:\\Users\\yaniv\\PycharmProjects\\pythonProject4\\google_docs'
os.environ['MY_ROOT_PATH'] = file_path


def read_files_in_directory():
    """
    Read files in a specified directory defined by the MY_ROOT_PATH environment variable.
    """
    root_directory = os.environ.get('MY_ROOT_PATH')
    for root, dirs, files in os.walk(root_directory):
        for file in files:
            file_path = os.path.join(root, file)
            read_file(file_path)


def read_file(file_path, encoding='latin-1'):
    """
    Read a file, handling Unicode decoding errors, and perform additional actions.

    :param file_path: Path to the file to be read.
    :param encoding: Encoding to use when reading the file.
    """
    try:
        with open(file_path, 'r', encoding=encoding) as file:
            for line_number, line in enumerate(file, start=1):
                insert_line_dict(line, file_path,line_number)
                insert_words_dict(line,file_path,line_number)
              # print(f"Line {line_number}: {line.strip()}")
    except UnicodeDecodeError:
        print(f"Error reading {file_path} with {encoding} encoding")


if __name__ == '__main__':
    read_files_in_directory()
