import sys

import search_mode
import read_files
import re


def insert_score_offset(line_result: str, sentence: str, score: int = 0) -> str:
    index = line_result.find(sentence)
    line = line_result + ' ,score = ' + str(len(line_result) * 2 - score) + ', offset = ' + str(index)
    return line


def results_search(sentence: str, dict_line: dict, dict_words: dict) -> list:
    """

    :param sentence: sentence to look for from data
    :param dict_line:
    :param dict_words:
    :return: A list of 5 sentences containing the sentence
    """
    all_result = search_mode.search_engine(sentence, dict_words)
    result = search_mode.extract_5_members(dict_line, all_result)

    if len(result) < 5:
        change_letters_list = []#complete_lists(sentence, dict_words.keys())
        for words in change_letters_list:
            all_result = search_mode.search_engine(words[0], dict_words)
            temp_result = search_mode.extract_5_members(dict_line, all_result)
            result += temp_result
            if len(result) >= 5:
                result = result[:5]
                break
    result_with_score_offset = []
    for res in result:
        result_with_score_offset.append(insert_score_offset(res, sentence))

    return result_with_score_offset


def main():
    if len(sys.argv) < 2:
        print("pathless")
        return
    path = sys.argv[1]
    dict_line = {}
    dict_words = {}
    read_files.read_files_in_directory(dict_line, dict_words, path)
    user_input = ""
    print("Enter a search")
    while True:
        user_input += input()
        if user_input.endswith('#exit#'):
            break
        if user_input.endswith('#'):
            user_input = ""
            print("Enter a search")
        if user_input != "":
            user_input = re.sub(r'[^a-zA-Z0-9]', ' ', user_input)
            user_input = re.sub(r'\s+', ' ', user_input).strip()
            user_input = user_input.lower()
            # all_result = search_mode.search_engine(user_input, dict_words)
            # result = search_mode.extract_5_members(dict_line, all_result)
            result = results_search(user_input, dict_line, dict_words)
            print_list(result)
            print("Continue the search or press # for a new search or #exit# to exit")
            print(user_input, end="")


def print_list(list_result):
    text = "The search yielded the following results:\n"
    if len(list_result) == 0:
        text += "No match found"
    for index in range(len(list_result)):
        text += str(index + 1) + ": " + list_result[index] + "\n"
    print(text)


if __name__ == "__main__":
    main()
