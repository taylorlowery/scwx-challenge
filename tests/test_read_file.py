import pytest
from lib.largest_word import read_file, get_longest_word
from config import LOG

def test_read_file(tmpdir):
    LOG.info("test_read_file()")
    file_contents = "a\nab\nabc\nabcd\nabcde"
    expected = file_contents.split()
    test_file = tmpdir.join("test_file.txt")
    test_file.write(file_contents)
    actual = read_file(test_file)
    LOG.debug(actual)
    assert actual == expected

def test_read_file_spaces(tmpdir):
    LOG.info("test_read_file_spaces")
    file_contents = "a ab abc abcd abcde"
    expected = file_contents.split()
    test_file = tmpdir.join("test_file.txt")
    test_file.write(file_contents)
    actual = read_file(test_file)
    assert actual == expected

@pytest.mark.read_file
def test_read_file_bad_filepath():
    LOG.info("test_read_file_bad_filepath()")
    file = ""
    with pytest.raises(FileNotFoundError) as e:
        read_file(file)