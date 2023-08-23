from clear_text import remove_non_alnum


def insert_line_dict(line: str, path: str, num_line: int, dict_line: dict) -> None:
    """
    Inserting a line into the dictionary, path and num line are keys
    :param line: data of line
    :param path: path of file
    :param num_line: num of line
    """
    if line != "" and line != '\n':
        new_line = line.replace('\n', '')
        dict_line[path, num_line] = new_line


def insert_words_dict(line: str, path: str, num_line: int, dict_words: dict) -> None:
    """
    Inserting words into the dictionary

    For example - insert_word_dict("I love py", 'about.txt', 10)
    {'i': {'love': [('about.txt', 10, 0)]}, 'love':
     {'py': [('about.txt', 10, 1)]}, 'py': {'': [('about.txt', 10, 2)]}}
    :param line: data of line
    :param path: path of file
    :param num_line: num of line
    """
    words = line.split()

    for i in range(len(words) - 1):
        word = remove_non_alnum(words[i].lower())
        next_word = remove_non_alnum(" ".join(words[i + 1: i + 2]).lower())

        if word not in dict_words:
            dict_words[word] = {}
        next_word_dict = dict_words[word]

        location = (path, num_line, i)
        if next_word not in next_word_dict:
            next_word_dict[next_word] = [location]
        else:
            next_word_dict[next_word].append(location)

        dict_words[word] = next_word_dict

    # for last word in line
    if words:
        location = (path, num_line, len(words) - 1)
        last_word = remove_non_alnum(words[-1].lower())
        if last_word not in dict_words:
            dict_words[last_word] = {"": [location]}
        else:
            next_word_dict = dict_words[last_word]
            if "" not in next_word_dict:
                next_word_dict[""] = [location]
            else:
                next_word_dict[""].append(location)

            dict_words[last_word] = next_word_dict
