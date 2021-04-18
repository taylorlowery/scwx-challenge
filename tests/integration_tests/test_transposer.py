import pytest
from config import LOG


def test_transpose_single_file(transposer_fixture):
    LOG.info("test_transpose_single_file()")
    data = transposer_fixture.transpose("./test_files/positive/abcde.txt")
    LOG.debug(data)

def test_transpose_empty_file(transposer_fixture):
    LOG.info("test_transpose_empty_file()")
    with pytest.raises(Exception) as e:
        (longest, transposed) = transposer_fixture.transpose("./test_files/negative/empty.txt")

def test_transpose_newlines(transposer_fixture):
    LOG.info("test_transpose_newlines()")
    with pytest.raises(Exception) as e:
        (longest, transposed) = transposer_fixture.transpose("./test_files/negative/newlines.txt")