from logging import ERROR
import os
from lib.utils import read_file, get_longest_word, reverse_string, get_txt_files_in_directory


'''
encapsulates methods for scwx challenge to find largest word in file, transpose it, and display both
possible improvements: 
configuration options for cleaning text (ex: remove end-of-line punctuation) and splitting text
ability to inject/change configuration
'''


class Transposer():

    def __init__(self):
        pass

    # Read the contents of a file, find the longest word, reverse(transpose) the word
    # return the longest and transposed word
    def get_longest_and_transposed_word_from_file(self, filepath):

        file_contents = read_file(filepath)
        if len(file_contents) == 0:
            raise Exception(f"{filepath} is empty")
        longest = get_longest_word(file_contents)
        reversed_word = reverse_string(longest)
        return (longest, reversed_word)

    # given a path to a file or directory, yield the longest word of each file
    def transpose(self, path):
        transposition = ""
        filepaths = []
        try:
            if os.path.isdir(path):
                files = get_txt_files_in_directory(path)
                if len(files) == 0:
                    return "This directory contains no .txt files"
                for file in files:
                    filepaths.append(os.path.join(path, file))
            elif os.path.isfile(path):
                if not path.endswith(".txt"):
                    return "The supplied file must be a .txt"
                filepaths.append(path)
            else:
                return "Invalid path"
        except OSError as oe:
            transposition += str(oe)
        except PermissionError as pe:
            transposition += str(pe)
        except Exception as e:
            transposition += str(e)
        for file in filepaths:
            try:
                transposition += f"Transposition for { file }:\n"
                (longest, reversed_word) = Transposer().get_longest_and_transposed_word_from_file(file)
                transposition += f"{longest}\n{reversed_word}\n"
            except Exception as e:
                transposition += f"{str(e)}\n"
            transposition += "============================\n"
        return transposition
