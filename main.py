import insert_data
import search_mode
import read_files
import re


def main():
    read_files.read_files_in_directory()
    user_input = ""
    running = True
    while running:
        print("Enter a search")
        if user_input != "":
            print(user_input, end="")
        user_input += input()
        if user_input.endswith('#'):
            running = False
        user_input = re.sub(r'[^a-zA-Z0-9]', ' ', user_input)
        user_input = re.sub(r'\s+', ' ', user_input).strip()

        all_result = search_mode.search_engine(user_input, insert_data.words_dict)
        result = search_mode.extract_5_members(insert_data.line_dict, all_result)
        print(result)


if __name__ == "__main__":
    main()
