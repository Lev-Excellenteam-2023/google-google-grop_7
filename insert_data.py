line_dict = {}
words_dict = {}


def insert_line_dict(line: str, path: str, num_line: int) -> None:
    """
    Inserting a line into the dictionary, path and num line are keys
    :param line: data of line
    :param path: path of file
    :param num_line: num of line
    """
    if line != "" and line != '\n':
        new_line = line.replace('\n', '')
        line_dict[path, num_line] = new_line


def insert_words_dict(line: str, path: str, num_line: int) -> None:
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

        if word not in words_dict:
            words_dict[word] = {}
        next_word_dict = words_dict[word]

        location = (path, num_line, i)
        if next_word not in next_word_dict:
            next_word_dict[next_word] = [location]
        else:
            next_word_dict[next_word].append(location)

        words_dict[word] = next_word_dict

    # for last word in line
    if words:
        location = (path, num_line, len(words) - 1)
        last_word = remove_non_alnum(words[-1].lower())
        if last_word not in words_dict:
            words_dict[last_word] = {"": [location]}
        else:
            words_dict[last_word][""].append(location)


def remove_non_alnum(word: str) -> str:
    """
    Remove char from word if not isalnum
    :param word:
    :return: word after removing
    """
    if word.isalnum():
        return word
    new_word = ""
    for ch in word:
        if ch.isalnum():
            new_word += ch

    return new_word
