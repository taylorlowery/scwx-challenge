from transposer import Transposer

def transpose(path):
    try:
        (longest, transposed) = Transposer().get_longest_and_transposed_word_from_file(path)
        print(longest)
        print(transposed)
    except Exception as e:
        print(e)


transpose("./test_files/abcde.txt")
transpose("./test_files")
# transpose("./test_files/abcde.txt")
# transpose("./test_files/ugly.txt")
# transpose("./test_files/doubles.txt")
# transpose("./test_files/integers.txt")
# transpose("./test_files/languages.txt")
# transpose("./test_files/length_tie.txt")
# transpose("./test_files/symbols.txt")
# transpose("./test_files/emojis.txt")
# transpose("./test_files/newlines.txt")
# transpose("./test_files/empty.txt")