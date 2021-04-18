import os
from transposer import Transposer
from lib.utils import get_txt_files_in_directory


# given a path to a file or directory, yield the longest word of each file
def transpose(path):
    transposition = ""
    filepaths = []
    if os.path.isdir(path):
        files = get_txt_files_in_directory(path)
        if len(files) == 0:
            transposition += "This directory contains no files"
        for file in files:
            filepaths.append(f"{path}/{file}")
    elif os.path.isfile(path):
        filepaths.append(path)
    else:
        transposition += "Invalid path"
    for file in filepaths:
        try:
            transposition += f"Transposition for { file }:\n"
            (longest, reversed_word) = Transposer().get_longest_and_transposed_word_from_file(file)
            transposition += f"{longest}\n{reversed_word}\n"
        except Exception as e:
            transposition += f"{str(e)}\n"
        transposition += "============================\n"
    return transposition


if __name__ == "__main__":
    print(transpose("./test_files/positive"))
