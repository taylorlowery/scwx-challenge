# Secureworks QA Automation Engineer Coding Challenge

## The Coding Challenge: 
1. Read input from a file of words
2. Find the largest word in the file
3. Transpose the letters in the largest word
4. Show the largest word and the largest word transposed 
5. Demonstrate positive and negative test cases
6. Ensure you document code and instructions for building and running based on the response best practices above

### Example file:
```
a
ab
abc
abcd
abcde
```

### Example output:
```
abcde
edcba
```

## Assumptions
For the purposes of this challenge, I assumed that all text input would be submitted as .txt files, and that the strings in the text input would be separated by standard english whitespace (ex: spaces, tabs, and newlines). I did not attempt to account punctuation in this implementation, so punctuation characters are counted as part of a word(ex: "Hello!" is counted as a 6-letter word).

## Description of Solution
This solution centers around a Transposer class (transposer.py) that makes use of the methods in lib.utils.py to get all the .txt files in a given directory, open and read each .txt file, find the longest string in each file, and transpose(reverse) that longest string. Finally, it prints the longest string and its transposition. Future improvements to this class could include methods for cleaning txt files before searching for the longest word (for example, to remove punctuation) or a different schema for splitting text than whitespace (for example, to accommodate Lao and Vietnamese documents).

The transpose method is accessed through main.py as a script. If supplied a path to an individual .txt file, it will print the longest word and its transposition found in that file; if given a path to a directory, it will check the directory for .txt files and transpose() any that it finds. Bad paths and empty directories will print warnings. If supplied no path, main.py will print the transposition for a sample file that fulfills the example output as described in the challenge above. 

## Prerequisites

### [Python 3.8 or higher](https://www.python.org/downloads/)
### [Pip](https://pip.pypa.io/en/stable/installing/#upgrading-pip) - _Pip should already be installed with Python 3.4 or higher, but here's the installation instructions, just in case_
### [VS Code](https://code.visualstudio.com/)

## Instructions
1. Clone Repo
2. Open Repo in VS Code
3. Open Terminal
4. Upgrade pip
4. Create & Activate Virtual Environment
5. Install requirements
5. Run main.py on default
6. Run main.py on sample.txt
7. Run main.py on absolute path to own file
8. Run tests
9. Deactivate Virtual Environment
