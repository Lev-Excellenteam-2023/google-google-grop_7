line_dict = {}
word_dict = {}


def insert_line_dict(line: str, path: str, num_line: int) -> None:
    """
    Inserting a line into the dictionary, path and num line are keys
    :param line: data of line
    :param path: path of file
    :param num_line: num of line
    """
    if line != "":
        line_dict[path, num_line] = line
