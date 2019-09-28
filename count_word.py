"""

Input Assumptions:


1. leading and trailing "," is ignored, ",," is ignored
2. word length is not checked. max word length is python array size limit.
    536870912 on 32 bit system
3. all characters are assumed ascii characters


Usage:

python count_word.py input_file word1 word2

Example:

$ python count_word.py tests/data/case1.in ab bc
ab 2
bc 2


"""

import sys
from services import FileWordCounter

if __name__ == '__main__':
    input_file = sys.argv[1]
    words = sys.argv[2:]

    file_word_counter = FileWordCounter(input_file)

    for word in words:
        print(f"{word},{file_word_counter.get_word_count(word)}")
