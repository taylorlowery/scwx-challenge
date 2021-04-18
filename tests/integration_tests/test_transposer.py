from attr import field
import pytest
from config import LOG


# running transpose on specific file produces expected results
@pytest.mark.transposer
@pytest.mark.parametrize("filename, expected_longest, expected_reverse",
                            [("abcde.txt", "abcde", "edcba"),
                                ("doubles.txt", "2412.21", "12.2142"),
                                ("emojis.txt", "💯😱😲🤠😒😗😀🏴󠁧󠁢󠁷󠁬󠁳󠁿", "💯😱😲🤠😒😗😀🏴󠁧󠁢󠁷󠁬󠁳󠁿"[::-1]),
                                ("integers.txt", "123456", "654321"),
                                ("languages.txt", "ΓειάσουΚόσμε", "εμσόΚυοσάιεΓ"),
                                ("length_tie.txt", "tuvwx", "xwvut"),
                                ("symbols.txt", ".#aCt!@#%@#$!^&", "&^!$#@%#@!tCa#."),
                                ("ugly.txt", "1234567890!@#$%^&*()-_=+[{]};:'\",<.>/?~Ѧ𝙱ƇᗞΣℱԍҤ١𝔍К𝓛𝓜ƝȎ𝚸𝑄Ṛ𝓢ṮṺƲᏔꓫ𝚈𝚭𝜶Ꮟçძ𝑒𝖿𝗀ḧ𝗂𝐣ҝɭḿ𝕟𝐨𝝔𝕢ṛ𝓼тú𝔳ẃ⤬𝝲𝗓", "1234567890!@#$%^&*()-_=+[{]};:'\",<.>/?~Ѧ𝙱ƇᗞΣℱԍҤ١𝔍К𝓛𝓜ƝȎ𝚸𝑄Ṛ𝓢ṮṺƲᏔꓫ𝚈𝚭𝜶Ꮟçძ𝑒𝖿𝗀ḧ𝗂𝐣ҝɭḿ𝕟𝐨𝝔𝕢ṛ𝓼тú𝔳ẃ⤬𝝲𝗓"[::-1])
                                ])
def test_transpose(transposer_fixture, filename, expected_longest, expected_reverse):
    LOG.info(f"test_transpose_single_file({ filename })")
    (longest, reversed_word) = transposer_fixture.get_longest_and_transposed_word_from_file(f"./test_files/{ filename }")
    assert longest == expected_longest
    assert reversed_word == expected_reverse


# running transpose on empty file raises error
@pytest.mark.transposer
def test_transpose_empty_file(transposer_fixture):
    LOG.info("test_transpose_empty_file()")
    with pytest.raises(Exception) as e:
        (longest, transposed) = transposer_fixture.get_longest_and_transposed_word_from_file("./test_files/empty.txt")


# running transpose on whitespace-only file raises error
@pytest.mark.transposer
def test_transpose_newlines(transposer_fixture):
    LOG.info("test_transpose_newlines()")
    with pytest.raises(Exception) as e:
        (longest, transposed) = transposer_fixture.get_longest_and_transposed_word_from_file("./test_files/newlines.txt")


# running transpose on empty directory returns string indicating error
@pytest.mark.transposer
def test_transpose_empty_dir(transposer_fixture):
    LOG.info("test_transpose_empty_dir()")
    expected = "This directory contains no .txt files"
    actual = transposer_fixture.transpose("./test_files/empty_dir")
    assert actual == expected


# running transpose on bad path returns string indicating error
@pytest.mark.transposer
def test_transpose_bad_path(transposer_fixture):
    LOG.info("test_transpose_bad_path()")
    expected = "Invalid path"
    actual = transposer_fixture.transpose("")
    assert actual == expected
