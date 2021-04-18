import os
from lib.utils import read_file, get_longest_word, reverse_string, get_txt_files_in_directory

class Transposer():
    
    def __init__(self):
        pass

    # Read the contents of a file, find the longest word, reverse(transpose) the word, and return the longest and transposed word
    def get_longest_and_transposed_word_from_file(self, filepath):
        try:
            file_contents = read_file(filepath)
            if len(file_contents) == 0:
                # TODO: Handle empty tile
                pass
            longest = get_longest_word(file_contents)
            reversed_word = reverse_string(longest)
            return (longest, reversed_word)
        except Exception as e:
            print(e)

    # given a path to a file or directory, yield the longest word of each file
    def transpose(self, path):
        if os.path.isdir(path):
            files = self.get_txt_files_in_directory(path)
            if len(files == 0):
                raise Exception("no files!")
            for file in files:
                yield self.get_longest_and_transposed_word_from_file(file)
        elif os.path.isfile(path):
            yield self.get_longest_and_transposed_word_from_file(path)
        else:
            raise Exception("Invalid path")