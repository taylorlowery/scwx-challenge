import pytest
import os
from lib.utils import get_txt_files_in_directory
from config import LOG


# returns txt files from mock file directory
@pytest.mark.get_txt_files
def test_get_txt_files_in_directory(mock_file_directory):
    LOG.info("test_get_txt_files_in_directory()")
    files = get_txt_files_in_directory(mock_file_directory)
    for file in files:
        LOG.debug(file)
    # TODO: assert filecount or names of files from mock_file_directory


# bad path raises file not found error
@pytest.mark.get_txt_files
def test_get_txt_files_in_directory_bad_path(mock_file_directory):
    LOG.info("test_get_txt_files_in_directory_bad_path()")
    # make sure the bad file path doesn't exist
    bad_file_path = os.path.join(mock_file_directory, "nonexistant_directory")
    if os.path.exists(bad_file_path):
        os.remove(bad_file_path)
    with pytest.raises(FileNotFoundError) as fe:
        get_txt_files_in_directory(bad_file_path)
