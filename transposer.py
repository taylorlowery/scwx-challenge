import os
from lib.utils import read_file, get_longest_word, reverse_string, get_txt_files_in_directory
from config import LOG

'''
encapsulates methods for scwx challenge to find largest word in file, transpose it, and display both
possible improvements: 
configuration options for cleaning text (ex: remove end-of-line punctuation) and splitting text
ability to inject/change configuration
'''
class Transposer():
    
    def __init__(self):
        pass

    # Read the contents of a file, find the longest word, reverse(transpose) the word, and return the longest and transposed word
    def get_longest_and_transposed_word_from_file(self, filepath):

        file_contents = read_file(filepath)
        LOG.debug(f"{filepath}: { file_contents }")
        if len(file_contents) == 0:
            raise Exception(f"{filepath} is empty")
        longest = get_longest_word(file_contents)
        reversed_word = reverse_string(longest)
        return (longest, reversed_word)

    # given a path to a file or directory, yield the longest word of each file
    def transpose(self, path):
        filepaths = []
        if os.path.isdir(path):
            files = get_txt_files_in_directory(path)
            if len(files) == 0:
                raise Exception("no files!")
            for file in files:
                filepaths.append(file)
        elif os.path.isfile(path):
            filepaths.append(path)
        else:
            raise Exception("Invalid path")
        for file in filepaths:
            print(f"Transposition for { file }")
            try:
                # try get longest transposed, if exception, print that
                thing = self.get_longest_and_transposed_word_from_file(f"{path}/{file}")
                yield thing
            except Exception as e:
                print(e)
