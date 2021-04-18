from lib.utils import get_txt_files_in_directory
from config import LOG

def test_get_txt_files_in_directory(mock_file_directory):
    files = get_txt_files_in_directory(mock_file_directory)
    for file in files:
        LOG.debug(file)