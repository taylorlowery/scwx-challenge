import pytest
import os
from config import LOG, ROOT_DIR


# running transpose on specific file produces expected results
@pytest.mark.transposer
@pytest.mark.parametrize("filename, expected_longest, expected_reverse",
                            [("abcde.txt", "abcde", "edcba"),
                                ("doubles.txt", "2412.21", "12.2142"),
                                ("emojis.txt", "๐ฏ๐ฑ๐ฒ๐ค ๐๐๐๐ด๓ ง๓ ข๓ ท๓ ฌ๓ ณ๓ ฟ", "๐ฏ๐ฑ๐ฒ๐ค ๐๐๐๐ด๓ ง๓ ข๓ ท๓ ฌ๓ ณ๓ ฟ"[::-1]),
                                ("integers.txt", "123456", "654321"),
                                ("languages.txt", "ฮฮตฮนฮฌฯฮฟฯฮฯฯฮผฮต", "ฮตฮผฯฯฮฯฮฟฯฮฌฮนฮตฮ"),
                                ("length_tie.txt", "tuvwx", "xwvut"),
                                ("symbols.txt", ".#aCt!@#%@#$!^&", "&^!$#@%#@!tCa#."),
                                ("ugly.txt", "1234567890!@#$%^&*()-_=+[{]};:'\",<.>/?~ัฆ๐ฑฦแฮฃโฑิาคูก๐ะ๐๐ฦศ๐ธ๐แน๐ขแนฎแนบฦฒแ๊ซ๐๐ญ๐ถแรงแซ๐๐ฟ๐แธง๐๐ฃาษญแธฟ๐๐จ๐๐ขแน๐ผัรบ๐ณแบโคฌ๐ฒ๐", "1234567890!@#$%^&*()-_=+[{]};:'\",<.>/?~ัฆ๐ฑฦแฮฃโฑิาคูก๐ะ๐๐ฦศ๐ธ๐แน๐ขแนฎแนบฦฒแ๊ซ๐๐ญ๐ถแรงแซ๐๐ฟ๐แธง๐๐ฃาษญแธฟ๐๐จ๐๐ขแน๐ผัรบ๐ณแบโคฌ๐ฒ๐"[::-1])
                                ])
def test_transpose(transposer_fixture, filename, expected_longest, expected_reverse):
    LOG.info(f"test_transpose_single_file({ filename })")
    (longest, reversed_word) = transposer_fixture.get_longest_and_transposed_word_from_file(os.path.join(ROOT_DIR, "sample_txt_files",  filename))
    assert longest == expected_longest
    assert reversed_word == expected_reverse


# running transpose on empty file raises Exception
@pytest.mark.transposer
def test_transpose_empty_file(transposer_fixture):
    LOG.info("test_transpose_empty_file()")
    with pytest.raises(Exception) as e:
        (longest, transposed) = transposer_fixture.get_longest_and_transposed_word_from_file(os.path.join(ROOT_DIR, "sample_txt_files", "empty.txt"))


# running transpose on whitespace-only file raises Exception
@pytest.mark.transposer
def test_transpose_newlines(transposer_fixture):
    LOG.info("test_transpose_newlines()")
    with pytest.raises(Exception) as e:
        (longest, transposed) = transposer_fixture.get_longest_and_transposed_word_from_file(os.path.join(ROOT_DIR, "sample_txt_files", "newlines.txt"))


# running transpose on empty directory returns string indicating error
@pytest.mark.transposer
def test_transpose_empty_dir(transposer_fixture):
    LOG.info("test_transpose_empty_dir()")
    expected = "This directory contains no .txt files"
    actual = transposer_fixture.transpose(os.path.join(ROOT_DIR, "sample_txt_files", "dir_no_txt"))
    assert actual == expected


# running transpose on bad path returns string indicating error
@pytest.mark.transposer
def test_transpose_bad_path(transposer_fixture):
    LOG.info("test_transpose_bad_path()")
    expected = "Invalid path"
    actual = transposer_fixture.transpose("")
    assert actual == expected


# running transpose on a non-.txt file returns string indicating error
@pytest.mark.transposer
def test_transpose_non_txt_file(transposer_fixture):
    LOG.info("test_transpose_non_txt_file()")
    expected = "The supplied file must be a .txt"
    actual = transposer_fixture.transpose(os.path.join(ROOT_DIR, "sample_txt_files", "dir_no_txt", "nada.py"))
    assert actual == expected
