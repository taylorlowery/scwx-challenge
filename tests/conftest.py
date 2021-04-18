import pytest
import os
from config import LOG
from transposer import Transposer

# create temporary file directory with sample text files for unit testing
@pytest.fixture(scope="session")
def mock_file_directory(tmpdir_factory):
    mock_file_dir = tmpdir_factory.mktemp("files")

    # create text file per challenge example
    abcde_txt = mock_file_dir.join("abcde.txt")
    abcde_txt.write("a\nab\nabc\nabcd\nabcde")

    # challenge example in random order
    abcde_random_txt = mock_file_dir.join("abcde_random.txt")
    abcde_random_txt.write("abc\nabcde\nab\na\nabcd")

    #separated by other whitespace characters
    abcde_whitespace_txt = mock_file_dir.join("abcde_whitespace.txt")
    abcde_whitespace_txt.write("a ab\tabc\fabcd\rabcde")
    
    #restricted permission file (unsuccessful)
    restricted_txt = mock_file_dir.join("restricted.txt")
    restricted_txt.write("This file should not be accessible.\n")
    # restricting the permissions on this file did not successfully trigger the PermissionError on read
    os.chmod(restricted_txt, 400)

    LOG.debug(f"Created mock file directory at { mock_file_dir }")
    return mock_file_dir

# create transposer to be used in tests
@pytest.fixture(scope="session")
def transposer_fixture():
    t = Transposer()
    return t