import pytest
from config import LOG


def transpose_single_file(transposer_fixture):
    LOG.info("transpose_single_file()")
    (longest, transposed) = transposer_fixture.get_longest_and_transposed_word_from_file("./test_files/abcde.txt")
    assert longest == "abcde"
    assert transposed == "edcba"
