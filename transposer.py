import os
from lib.utils import read_file, get_longest_word, reverse_string

class Transposer():
    
    def __init__(self):
        pass

    def get_files_in_directory(self, directory):
        pass

    # Read the contents of a file, find the longest word, reverse(transpose) the word, and return the longest and transposed word
    def get_longest_and_transposed_word_from_file(self, filepath):
        try:
            file_contents = read_file(filepath)
            longest = get_longest_word(file_contents)
            reversed_word = reverse_string(longest)
            return (longest, reversed_word)
        except Exception as e:
            print(e)
