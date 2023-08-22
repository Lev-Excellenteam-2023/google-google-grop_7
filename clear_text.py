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


def remove_non_alnum_lins(line: str) -> str:
    """
    Remove char from line if not isalnum
    :param line:
    :return: line after removing
    """
    new_line = ""
    text = line.split(" ")
    for ch in text:
        new_line += remove_non_alnum(ch) + " "

    return new_line
