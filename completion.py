from rapidfuzz.distance import Levenshtein


def calculate_score(original_word: str, new_word: str, offset: int):
    """
    Calculate the score for a single-letter difference between two words.

    :param original_word: The original word.
    :param new_word: The modified word with a single-letter difference.
    :param offset: The offset of the word in the full sentence.
    :return: The calculated score.
    """
    score = 0
    len_original_word = len(original_word)
    len_new_word = len(new_word)
    for i in range(min(len_original_word, len_new_word)):
        if original_word[i] != new_word[i]:
            score = score_to_index(i + offset)
            break
    # if there is adding or lacking of letter
    if len_original_word != len_new_word:
        # if the adding or lacking in the last letter
        if original_word[len_original_word - 1] != new_word[len_new_word - 1]:
            index = max(len_original_word, len_new_word)
            score = score_to_index(index)
        score = score * 2
    return score


def score_to_index(index):
    """
    Convert an index to a score based on the position.

    :param index: The index of the differing character.
    :return: The corresponding score.
    """
    if index == 0:
        return 5
    elif index == 1:
        return 4
    elif index == 2:
        return 3
    elif index == 3:
        return 2
    else:
        return 1


def get_similar_words(word: str, offset: int, words_list: list):
    """
    Find similar words with a single-letter difference and calculate their scores.

    :param word: The reference word.
    :param offset: The offset of the differing character.
    :param words_list: A list of words to search for similarities.
    :return: List of tuples containing similar word and calculated score.
    """
    single_letter_errors = []
    for ref_word in words_list:
        if Levenshtein.distance(word, ref_word) == 1:
            single_letter_errors.append((ref_word, calculate_score(ref_word, word, offset)))
    return single_letter_errors

