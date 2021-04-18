from lib.utils import read_file, get_longest_word, reverse_string


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
