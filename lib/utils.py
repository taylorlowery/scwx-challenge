# Open a file at a given filepath and return a list of its contents split on whitespace
import os
from config import LOG


# look at directory and return .txt files
def get_txt_files_in_directory(directory):
    files = os.listdir(directory)
    return [txt for txt in files if txt.endswith(".txt")]


# read contents at filepath and return its contents split on whitespace
def read_file(filepath):
    with open(file=filepath, mode="r", encoding="utf-8") as file:
        contents = file.read().split()
        return contents


# Take a list of strings, sort by length, and return the longest
def get_longest_word(words):
    if len(words) == 0:
        raise IndexError("No words were entered")
    for word in words:
        if not isinstance(word, str):
            raise TypeError(f"get_longest_word() expects strings, but got a type({ word })")
    longest_word = sorted(words, key=len)[-1]
    return longest_word


# Take a string as input and return it reversed (transposed)
def reverse_string(input):
    if not isinstance(input, str):
        raise TypeError(f"reverse_string() expects a string but got a { type(input) }")
    reversed_input = input[::-1]
    return reversed_input
