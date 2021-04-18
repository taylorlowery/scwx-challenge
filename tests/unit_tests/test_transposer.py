import pytest
from config import LOG

@pytest.mark.transposer
def test_transposer(mock_file_directory, transposer_fixture):
    transposed_data = transposer_fixture.transpose(mock_file_directory)
    for data in transposed_data:
        LOG.debug(data)
    # TODO: asserts for longest words in files