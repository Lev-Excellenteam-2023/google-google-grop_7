import sys

import search_mode
import read_files
import re


def main():
    dict_line = {}
    dict_words = {}
    read_files.read_files_in_directory(dict_line, dict_words)
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
            all_result = search_mode.search_engine(user_input, dict_words)
            result = search_mode.extract_5_members(dict_line, all_result)
            print_list(result)
            print("Continue the search or press # for a new search or #exit# to exit")
            print(user_input, end="")


def print_list(list):
    text = "The search yielded the following results:\n"
    for index in range(len(list)):
        text += str(index + 1) + ": " + list[index] + "\n"
    print(text)


if __name__ == "__main__":
    main()
