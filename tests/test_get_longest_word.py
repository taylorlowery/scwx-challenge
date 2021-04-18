import pytest
from lib.utils import get_longest_word
from config import LOG

# Get longest word from a string of characters
@pytest.mark.get_longest_word
@pytest.mark.parametrize("words, expected", [(["a", "ab", "abc"], "abc"), 
                                                (["a"], "a"),
                                                (["a", "b", "c"], "c"),
                                                (["c", "b", "a"], "a"),
                                                (["hello", "amigo", "mouse"], "mouse"),
                                                (["", "", "", "", ""], ""),
                                                (["abc", "ab", "a"], "abc"),
                                                (["abc", "abc.", "a"], "abc."),
                                                ([".#aCt!@#%@#$!^&", "!@#&><", "!4\\!#$"], ".#aCt!@#%@#$!^&"),
                                                (["ab", "abc", "a"], "abc"),
                                                (["hello world", "سلام دنیا", "Привіт Світ", "你好，世界", "Γειά σου Κόσμε", "नमस्कार संसार", "שלום עולם"], "Γειά σου Κόσμε"),
                                                (["lol🤣", "exaggeration", "abcde"], "exaggeration"),
                                                (["a", "b", "🤣"], "🤣"),
                                                ])
def test_get_longest_word(words, expected):
    LOG.info(f"test_get_longest_word({words}, {expected})")
    longest = get_longest_word(words)
    assert longest == expected

@pytest.mark.get_longest_word
def test_get_longest_word_empty_list():
    LOG.info("test_get_longest_word_empty_list()")
    with pytest.raises(IndexError) as ie:
        longest = get_longest_word([])
    error_msg = ie.value.args[0]
    assert error_msg == "No words were entered"

@pytest.mark.get_longest_word
@pytest.mark.parametrize("words, wrong_type_element", [(["a", 12, "abc"], 12), 
                                                        ([13, "a", "abc"], 13), 
                                                        (["a", "ab", True], True),
                                                        (["a", "ab", b"abc"], b"abc"),
                                                        ([bytearray(1), "ab", "abc"], bytearray(1)),
                                                        ])
def test_get_longest_word_incorrect_types(words, wrong_type_element):
    LOG.info(f"test_get_longest_word_incorrect_types({ wrong_type_element })")
    with pytest.raises(TypeError) as ve:
        longest = get_longest_word(words)
    error_msg = ve.value.args[0]
    LOG.debug(error_msg)