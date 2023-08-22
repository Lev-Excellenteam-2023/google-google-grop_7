import sys

import search_mode
import read_files
import re


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
            all_result = search_mode.search_engine(user_input, dict_words)
            result = search_mode.extract_5_members(dict_line, all_result)
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
