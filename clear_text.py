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
