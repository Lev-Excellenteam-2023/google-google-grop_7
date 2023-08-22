from unittest.mock import Mock
import completion


def test_completion_classic():
    mock_complete = Mock()
    mock_complete.get_similar_words = lambda text, offset, list_keywords: completion.get_similar_words(text, offset,
                                                                                                       list_keywords)
    assert set(mock_complete.get_similar_words('aaa', 0, ['aab', 'bbc', 'ccd'])) == {('aab', 3)}


def test_completion_empty():
    mock_complete = Mock()
    mock_complete.get_similar_words = lambda text, offset, list_keywords: completion.get_similar_words(text, offset,
                                                                                                       list_keywords)
    assert mock_complete.get_similar_words('aaa', 0, []) == []


def test_completion_single():
    mock_complete = Mock()
    mock_complete.calculate_score = lambda original_word, new_word, offset: completion.calculate_score(original_word,
                                                                                                       new_word, offset)
    assert mock_complete.calculate_score('aaa', 'aab', 0) == 3


def test_completion_2():
    mock_complete = Mock()
    mock_complete.calculate_score = lambda original_word, new_word, offset: completion.calculate_score(original_word,
                                                                                                       new_word, offset)
    assert mock_complete.calculate_score('aa', 'aaa', 0) == 6


def test_completion_3():
    mock_complete = Mock()
    mock_complete.calculate_score = lambda original_word, new_word, offset: completion.calculate_score(original_word,
                                                                                                       new_word, offset)
    assert mock_complete.calculate_score('aaa', 'aa', 0) == 6
