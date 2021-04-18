from transposer import Transposer

def transpose(path):
    try:
        (longest, transposed) = Transposer().get_longest_and_transposed_word_from_file(path)
        print(longest)
        print(transposed)
    except Exception as e:
        print(e)


transpose("./files/abcde.txt")