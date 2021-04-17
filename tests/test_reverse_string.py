import pytest
from lib.largest_word import reverse_string
from config import LOG

@pytest.mark.reverse_string
def test_reverse_string():
    LOG.info("test_reverse_string()")
    expected = "drow"
    actual = reverse_string("word")
    assert expected == actual

@pytest.mark.reverse_string
def test_reverse_string_long():
    LOG.info("test_reverse_string_long()")
    input = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
    expected = input[::-1]
    actual = reverse_string(input)
    assert expected == actual

@pytest.mark.reverse_string
def test_reverse_string_empty_string():
    LOG.info("test_reverse_string_empty_string()")
    expected = ""
    actual = reverse_string("")
    assert expected == actual

@pytest.mark.reverse_string
def test_reverse_string_escaped_characters():
    LOG.info("test_reverse_string_escaped_characters()")
    expected = "\f\b\t\r\n\"\\\'"
    actual = reverse_string("\'\\\"\n\r\t\b\f")
    assert expected == actual

@pytest.mark.reverse_string
def test_reverse_string_escaped_hex_values():
    LOG.info("test_reverse_string_escaped_hex_values()")
    expected = "\x31\x32\x33\x34"
    actual = reverse_string("\x34\x33\x32\x31")
    assert expected == actual

@pytest.mark.reverse_string
def test_reverse_string_escaped_ansi_color_code():
    LOG.info("test_reverse_string_escaped_ansi_color_code()")
    expected = "\033[1,37m"
    actual = reverse_string("m73,1[\033")
    assert expected == actual

@pytest.mark.reverse_string
@pytest.mark.parametrize("input", ["hello world", "سلام دنیا", "Привіт Світ", "你好，世界", "Γειά σου Κόσμε", "नमस्कार संसार", "שלום עולם"])
def test_reverse_string_other_languages(input):
    LOG.info(f"test_reverse_string_other_languages(\"{ input }\")")
    expected = "".join(reversed(input))
    actual = reverse_string(input)
    assert expected == actual

@pytest.mark.reverse_string
@pytest.mark.parametrize("input", [None, 1234, 1.0, 0, True, False, ["a", "b", "c"], ("a", "b", "c"), bytearray(5), b"Howdy!"])
def test_reverse_string_other_data_types_raise_value_error(input):
    LOG.info(f"test_reverse_string_other_data_types_raise_value_error({ input })")
    with pytest.raises(TypeError) as error_info:
        reverse_string(input)
    exception_actual = error_info.value
    LOG.debug(exception_actual)
    exception_expected = f"reverse_string() expects a string but got a { type(input) }"
    assert str(exception_actual) == exception_expected


