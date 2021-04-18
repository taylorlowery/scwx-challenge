import pytest
from lib.utils import get_longest_word
from config import LOG

@pytest.mark.parametrize("words, expected", [(["a", "ab", "abc"], "abc"), 
                                                (["a"], "a"),
                                                (["a", "b", "c"], "c"),
                                                (["c", "b", "a"], "a"),
                                                (["hello", "amigo", "mouse"], "mouse"),
                                                (["", "", "", "", ""], ""),
                                                (["abc", "ab", "a"], "abc"),
                                                (["ab", "abc", "a"], "abc"),
                                                (["hello world", "سلام دنیا", "Привіт Світ", "你好，世界", "Γειά σου Κόσμε", "नमस्कार संसार", "שלום עולם"], "Γειά σου Κόσμε"),
                                                (["lol🤣", "exaggeration", "abcde"], "exaggeration")
                                                ])
def test_get_longest_word(words, expected):
    LOG.info(f"test_get_longest_word({words}, {expected})")
    longest = get_longest_word(words)
    assert longest == expected

def test_get_longest_word_empty_list():
    LOG.info("test_get_longest_word_empty_list()")
    with pytest.raises(IndexError) as ie:
        longest = get_longest_word([])
    error_msg = ie.value.args[0]
    assert error_msg == "No words were entered"

def test_get_longest_word_incorrect_types():
    LOG.info("test_get_longest_word_incorrect_types()")
    with pytest.raises(TypeError) as ve:
        longest = get_longest_word(["a", 1, "bc"])