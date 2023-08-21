import insert_data
import search_mode
import read_files


def main():
    read_files.read_files_in_directory()
    user_input = ""
    while not (user_input.endswith('#')):
        print("Enter a search")
        if user_input != "":
            print(user_input, end="")
        user_input += input()
        list_input = user_input.split()
        user_input = ""
        for word in list_input:
            word = insert_data.remove_non_alnum(word)


        user_input = insert_data.remove_non_alnum(user_input)

        all_result = search_mode.search_engine(user_input, insert_data.words_dict)
        result = search_mode.extract_5_members(insert_data.line_dict, all_result)
        print(result)


if __name__ == "__main__":
    main()
