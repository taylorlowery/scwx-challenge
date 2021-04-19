import os
import sys
from transposer import Transposer
from config import ROOT_DIR


# given a path to a file or directory, yield the longest word of each file
def transpose(path):
    return Transposer().transpose(path)


if __name__ == "__main__":
    path = os.path.join(ROOT_DIR, "sample_txt_files", "abcde.txt")
    print(sys.argv)
    if len(sys.argv) >= 2:
        path = sys.argv[1]
    print(transpose(path))
