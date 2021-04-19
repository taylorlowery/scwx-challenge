# Secureworks QA Automation Engineer Coding Challenge

## The Coding Challenge: 
1. Read input from a file of words
2. Find the largest word in the file
3. Transpose the letters in the largest word
4. Show the largest word and the largest word transposed 
5. Demonstrate positive and negative test cases
6. Ensure you document code and instructions for building and running based on the response best practices above

### Example input file contents:
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
For the purposes of this challenge, I assumed that all text input would be submitted as .txt files, and that the strings in the text input would be separated by standard english whitespace (ex: spaces, tabs, and newlines). I did not attempt to account for punctuation in this implementation, so punctuation characters are counted as part of a word(ex: "Hello!" is counted as a 6-letter word). Lastly, if there multiple words that tie for the longest length, the last word is printed.

## Description of Solution
This solution centers around a Transposer class (transposer.py) that makes use of the methods in lib.utils.py to find, open and read .txt files, find the longest string in each file, and transpose(reverse) that longest string. Finally, Transposer prints the longest string and its transposition. Future improvements to this class could include methods for cleaning text input before searching for the longest word (for example, to remove punctuation) or a different schema for splitting text than whitespace (for example, to accommodate Lao and Vietnamese documents).

The solution works by passing a path to a .txt file or a directory to the project's main.py. If main.py is supplied a path to an individual .txt file, it will print the longest word found in that file and its transposition; if given a path to a directory, it will check the directory for .txt files and transpose any that it finds. Bad paths and empty directories will print error messages. If supplied no path, main.py will print the transposition for a sample file that fulfills the example output as described in the challenge above. 

## Prerequisites

### [Python 3.8 or higher](https://www.python.org/downloads/)
### [Pip](https://pip.pypa.io/en/stable/installing/)
_Pip should already be installed with Python 3.4 or higher, but here's the installation instructions, just in case_
### [Venv](https://docs.python.org/3/library/venv.html#module-venv)
_should also be installed with Python_
### [VS Code](https://code.visualstudio.com/)

## Instructions
_The following instructions should work on Windows, Mac, and Linux systems. Depending on your configuration, you may need to elevate to administrator privileges._
### 1. Open a terminal and navigate to the directory where you'd like to clone a git repo.
### 2. Clone this repository to that directory:
```
git clone https://github.com/taylorlowery/scwx-challenge.git
```
### 3. Navigate into the project directory:
```
cd scwx-challenge
```
### 4. Upgrade pip:
```
python -m pip install -U pip
```
### 4. Create & Activate Virtual Environment
```
python -m venv venv
```
To activate on windows, enter the following command:
```
.\venv\Scripts\activate
```
For Mac and Linux: 
```
source venv/bin/activate
```
### 5. Install requirements
```
pip install -r requirements.txt
```
### 6. Try out the Transposer with default implementation:
```
python main.py
```
This runs the Transposer on a sample file that happens to fulfill the challenge example, and should print: 
```
Transposition for abcde.txt:
abcde
edcba
```
If you look in the sample_txt_files directory, you'll see a number of .txt files that you can try the Transposer out on:
```
python main.py ./sample_txt_files/emojis.txt
```
or you can run the Transposer on the whole directory, printing out the transposition for each .txt file:
```
python main.py ./sample_txt_files
```
Lastly, you can run the transposer on an absolute path to your own file or directory. For example:
```
python main.py "C:\Users\{ you }\Desktop\absolutepath.txt"
```
### 8. Run the tests!
The tests directory contains folders for unit tests and integration tests. The unit tests cover the methods in lib.utils.py, and instead of accessing the file system, they use a mock/temporary directory defined as a fixture in conftest.py. The integration tests cover the Transposer, and run tests against the .txt documents in the sample_txt_files directory. Since the Transposer currently holds no state, all the tests use a transposer that is also defined as a fixture in conftest.py. 
In the future, test coverage could be improved by writing unit tests for the transposer that use the mock file directory rather than sample_txt_files, as well as expanding the variety of files in the mock file directory.
If configuration or other functionality were added to the Transposer in the future, using a fixture would probably not be a suitable approach. 
To run all the tests, from the root of the project folder, you just need to "pytest" the path to the directory or file containing the tests you wish to run: 
```
# all tests
pytest ./tests

# just the integration tests:
pytest ./tests/integration_tests

# just the unit tests: 
pytest ./tests/unit_tests

# a single test document
pytest ./tests/unit_tests/test_get_longest_word.py
```
All the tests are also marked so that the user can run subsets of the tests. The full list of markers can be found under "markers" in pytest.ini. A subset of marked tests can be run or excluded like so:
```
# run only the transposer tests
pytest -v -m transposer ./tests

# run all except the transposer tests
pytest -v -m "not transposer" ./tests
```

### 9. Remember to deactivate your Virtual Environment:
```
deactivate
```
