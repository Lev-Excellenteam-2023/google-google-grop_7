from unittest.mock import Mock
import complete_lists


def test_offset_location():
    mock_offset = Mock()
    mock_offset.offset_location = lambda text, index: complete_lists.offset_location(text, index)
    assert mock_offset.offset_location('a b c', 0) == 0


def test_offset_location_2():
    mock_offset = Mock()
    mock_offset.offset_location = lambda text, index: complete_lists.offset_location(text, index)
    assert mock_offset.offset_location('a b c', 1) == 2


def test_offset_location_3():
    mock_offset = Mock()
    mock_offset.offset_location = lambda text, index: complete_lists.offset_location(text, index)
    assert mock_offset.offset_location('', 0) == 0


def test_complete_lists():
    mock_complete = Mock()
    mock_complete.complete_lists = lambda text, list_keywords: complete_lists.complete_lists(text, list_keywords)
    assert (set((mock_complete.complete_lists('aaa bbb ccc', ['aab', 'bbc', 'ccd']))) ==
            {('aab bbb ccc', 3), ('aaa bbc ccc', 1), ('aaa bbb ccd', 1)})


def test_complete_lists_2():
    mock_complete = Mock()
    mock_complete.complete_lists = lambda text, list_keywords: complete_lists.complete_lists(text, list_keywords)
    assert (set((mock_complete.complete_lists('aaa bbb ccc', ['aaa', 'bbb', 'ccc']))) == set())


def test_complete_lists_3():
    mock_complete = Mock()
    mock_complete.complete_lists = lambda text, list_keywords: complete_lists.complete_lists(text, list_keywords)
    assert ((set((mock_complete.complete_lists('aaa bbb ccc', ['baa', 'cbb', 'dcc', 'edd'])))) ==
            {('baa bbb ccc', 5), ('aaa cbb ccc', 1), ('aaa bbb dcc', 1)})
