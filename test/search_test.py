from unittest.mock import Mock
import search_mode


def test_search_engine_classic():
    mock_search = Mock()
    dictionary = {'a': {'b': [('file1', 1, 0), ('file2', 2, 0), ('file3', 3, 0)]}}
    mock_search.search_engine = lambda text, dictionary: search_mode.search_engine(text, dictionary)
    assert set(mock_search.search_engine('a b', dictionary)) == {('file1', 1), ('file2', 2), ('file3', 3)}


def test_search_engine_empty():
    mock_search = Mock()
    dictionary = {'a': {'b': [('file1', 1, 0), ('file2', 2, 0), ('file3', 3, 0)]}}
    mock_search.search_engine = lambda text, dictionary: search_mode.search_engine(text, dictionary)
    assert mock_search.search_engine('a c', dictionary) == []


def test_search_engine_single():
    mock_search = Mock()
    dictionary = {'a': {'b': [('file1', 1, 0), ('file2', 2, 0), ('file3', 3, 0)]},
                  'c': {'d': [('file4', 4, 0), ('file5', 5, 0), ('file6', 6, 0)]}}
    mock_search.search_engine = lambda text, dictionary: search_mode.search_engine(text, dictionary)
    assert set(mock_search.search_engine('a', dictionary)) == {('file1', 1), ('file2', 2), ('file3', 3)}


def test_search_engine_2():
    mock_search = Mock()
    dictionary = {'a': {'b': [('file1', 1, 0), ('file2', 2, 0), ('file3', 3, 0)]},
                  'c': {'d': [('file1', 1, 2), ('file5', 5, 3), ('file1', 1, 2)]},
                  'b': {'c': [('file1', 1, 1), ('file1', 11, 2), ('file1', 1, 1)]}}
    mock_search.search_engine = lambda text, dictionary: search_mode.search_engine(text, dictionary)
    a = mock_search.search_engine('a b c', dictionary)
    assert set(mock_search.search_engine('a b c', dictionary)) == {('file1', 1)}


def test_search_engine_3():
    mock_search = Mock()
    dictionary = {'a': {'b': [('file1', 1, 0), ('file2', 2, 0), ('file3', 3, 0)]},
                  'b': {'c': [('file1', 1, 1), ('file2', 2, 1), ('file3', 11, 2)]},
                  'c': {'d': [('file1', 1, 2), ('file2', 2, 2), ('file3', 1, 2)]},
                  'd': {'e': [('file1', 1, 3), ('file2', 2, 3), ('file3', 1, 1)]},
                  'e': {'f': [('file1', 1, 4), ('file2', 2, 4), ('file3', 1, 1)]}}
    mock_search.search_engine = lambda text, dictionary: search_mode.search_engine(text, dictionary)
    assert set(mock_search.search_engine('a b c d e', dictionary)) == {('file1', 1), ('file2', 2)}


def test_search_engine_4():
    mock_search = Mock()
    dictionary = {'a': {'b': [('file1', 1, 0), ('file2', 2, 0), ('file3', 3, 0)]},
                  'b': {'c': [('file1', 1, 1), ('file2', 2, 1), ('file3', 3, 1)]},
                  'c': {'d': [('file1', 1, 2), ('file2', 2, 2), ('file3', 3, 2)]},
                  'd': {'e': [('file1', 1, 3), ('file2', 2, 3), ('file3', 3, 3)]},
                  'e': {'f': [('file1', 1, 4), ('file2', 2, 4), ('file3', 3, 4)]}}
    mock_search.search_engine = lambda text, dictionary: search_mode.search_engine(text, dictionary)
    assert set(mock_search.search_engine('a b c d e', dictionary)) == {('file1', 1), ('file2', 2), ('file3', 3)}


def test_search_engine_single_empty():
    mock_search = Mock()
    dictionary = {'a': {'b': [('file1', 1, 0), ('file2', 2, 0), ('file3', 3, 0)]},
                  'c': {'d': [('file4', 4, 0), ('file5', 5, 0), ('file6', 6, 0)]}}
    mock_search.search_engine = lambda text, dictionary: search_mode.search_engine(text, dictionary)
    assert mock_search.search_engine('e', dictionary) == []


def test_extract_5_members_empty():
    mock_search = Mock()
    dictionary = {'a': {'b': [('file1', 1, 0), ('file2', 2, 0), ('file3', 3, 0)]},
                  'c': {'d': [('file4', 4, 0), ('file5', 5, 0), ('file6', 6, 0)]}}
    mock_search.extract_5_members = lambda input_dict, key_list: search_mode.extract_5_members(input_dict, key_list)
    assert mock_search.extract_5_members(dictionary, ['e']) == []


def test_extract_5_members():
    mock_search = Mock()
    dictionary = {('a', 1): "aaaaa", ('a', 2): "aaaab", ('a', 3): "aaabb", ('a', 4): "aabbb", ('a', 5): "abbbb"}
    mock_search.extract_5_members = lambda input_dict, key_list: search_mode.extract_5_members(input_dict, key_list)
    assert mock_search.extract_5_members(dictionary, [('a', 1)]) == ["aaaaa"]


def test_extract_5_members_2():
    mock_search = Mock()
    dictionary = {('a', 1): "aaaaa", ('a', 2): "aaaab", ('a', 3): "aaabb", ('a', 4): "aabbb", ('a', 5): "abbbb"}
    mock_search.extract_5_members = lambda input_dict, key_list: search_mode.extract_5_members(input_dict, key_list)
    assert mock_search.extract_5_members(dictionary, [('a', 1), ('a', 2)]) == ["aaaaa ('a', 1)", "aaaab ('a', 2)"]


def test_extract_5_members_3():
    mock_search = Mock()
    dictionary = {('a', 1): "aaaaa", ('a', 2): "aaaab", ('a', 3): "aaabb", ('a', 4): "aabbb", ('a', 5): "abbbb",
                  ('a', 6): "bbbbb", ('a', 7): "bbbbc"}
    mock_search.extract_5_members = lambda input_dict, key_list: search_mode.extract_5_members(input_dict, key_list)
    assert (mock_search.extract_5_members(dictionary,
                                          [('a', 7), ('a', 6), ('a', 5), ('a', 4), ('a', 3), ('a', 1), ('a', 2)]) == [
                "aaaaa ('a', 1)", "aaaab ('a', 2)", "aaabb ('a', 3)", "aabbb ('a', 4)", "abbbb ('a', 5)"])
