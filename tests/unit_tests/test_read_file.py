import pytest
from lib.utils import read_file, get_longest_word
from config import LOG

# read file separated by newlines
def test_read_file(tmpdir):
    LOG.info("test_read_file()")
    file_contents = "a\nab\nabc\nabcd\nabcde"
    expected = file_contents.split()
    # create temp file for testing
    test_file = tmpdir.join("test_file.txt")
    test_file.write(file_contents)
    # read temp file
    actual = read_file(test_file)
    LOG.debug(actual)
    assert actual == expected

# read file separated by spaces
def test_read_file_spaces(mock_file_directory):
    LOG.info("test_read_file_from_mock_dir()")
    file_contents = "a ab abc abcd abcde"
    expected = file_contents.split()
    test_file = f"{ mock_file_directory }/abcde.txt"
    actual = read_file(test_file)
    assert actual == expected

# read a file with mixed whitespace
def test_read_file_mixed_whitespace(mock_file_directory):
    LOG.info("test_read_file_from_mock_dir()")
    file_contents = "a ab abc abcd abcde"
    expected = file_contents.split()
    test_file = f"{ mock_file_directory }/abcde_whitespace.txt"
    actual = read_file(test_file)
    assert actual == expected

# read from file that doesn't exist
@pytest.mark.read_file
def test_read_file_bad_filepath(mock_file_directory):
    LOG.info("test_read_file_bad_filepath()")
    file = f"{ mock_file_directory }/badfilepath.txt"
    with pytest.raises(FileNotFoundError) as e:
        read_file(file)
    LOG.debug(e)

# attempting to read a restricted file should raise a PermissionError
# TODO: simulate permission restriction in mock_file_directory
@pytest.mark.xfail
@pytest.mark.read_file
def test_read_file_restricted_file(mock_file_directory):
    LOG.info("test_read_file_restricted_file()")
    file = f"{ mock_file_directory }/restricted.txt"
    with pytest.raises(PermissionError) as e:
        read_file(file)

