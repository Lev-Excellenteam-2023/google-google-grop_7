def search_engine(text: str, dictionary: dict) -> list:
    """
    :param text: from the user
    :param dictionary: from the database
    :return: list of tuples with the name of the file and the number of the line
    """
    words = text.split(" ")
    set_of_tuples = set()

    # Handle the case when only one word is present in the input
    if words[0] in dictionary and len(words) == 1:
        # Return all tuples associated with the first word in the dictionary
        set_of_tuples = [tup for sublist in dictionary[words[0]].values() for tup in sublist]
        return [(filename, line_number) for filename, line_number, count in set_of_tuples]

    # Check if the first two words exist in the dictionary
    if words[0] in dictionary and words[1] in dictionary[words[0]]:
        set_of_tuples = set(dictionary[words[0]][words[1]])
        # Increment the count value for each tuple
        set_of_tuples = [(filename, line_number, count + 1) for filename, line_number, count in set_of_tuples]
    else:
        # No matches found, return an empty result
        return []

    # Iterate through subsequent words to narrow down the search
    for word in range(1, len(words) - 1):
        if words[word] in dictionary and words[word + 1] in dictionary[words[word]]:
            # Intersect the set of tuples with new search results
            set_temp = set(dictionary[words[word]][words[word+1]])
            set_intersection = set_temp.intersection(set_of_tuples)
            # Increment the count value for each tuple
            set_of_tuples = [(filename, line_number, count + 1) for filename, line_number, count in set_intersection]

    # Create the final result list with filenames and line numbers
    res = [(filename, line_number) for filename, line_number, count in set_of_tuples]
    return res


def extract_5_members(input_dict, key_list):
    result_list = []

    for key in key_list:
        if key in input_dict:
            result_list.append(input_dict[key] + " " + str(key))

    result_list.sort()  # Sort the extracted values
    return result_list[:5]
