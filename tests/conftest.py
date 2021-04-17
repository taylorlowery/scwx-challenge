import pytest
from config import LOG

@pytest.fixture(scope="session")
def mock_file_directory(tmpdir_factory):
    mock_file_dir = tmpdir_factory.mktemp("files")
    # create text file per challenge example
    abcde_txt = mock_file_dir.join("abcde.txt")
    abcde_txt.write("a\nab\nabc\nabcd\nabcde")
    # other test files
    abcde_random_txt = mock_file_dir.join("abcde_random.txt")
    abcde_random_txt.write("abc\nabcde\nab\na\nabcd")
    LOG.debug(f"Created mock file directory at { mock_file_dir }")
    return mock_file_dir

