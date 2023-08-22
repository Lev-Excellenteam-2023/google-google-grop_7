
def offset_location(text: str, index: int):
    """
    Return the offset of the word in the text.
    :param text:
    :param index:
    :return:
    """
    words = text.split(" ")
    offset = 0
    for i in range(index):
        offset += len(words[i]) + 1
    return offset


def complete_lists(text: str, list_keywords: list):
    tup_list = []
    words = text.split(" ")
    for index in range(len(words)):
        offset = offset_location(text, index)
        # function(words, offset, list_keywords)
        # tupls = [(word, score), (), ()....]
        tupls = []
        for tup_i in range(len(tupls)):
            line = words.copy()
            line[index] = tupls[tup_i][0]
            line = " ".join(line)
            tupls[tup_i] = (line, tupls[tup_i][1])

        tup_list.append(tupls)

    return sorted(tup_list, key=lambda x: x[2])
