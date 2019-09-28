"""
Usage:

python count_word.py input_file word1 word2

"""

import sys
from services import FileWordCounter

if __name__ == '__main__':
    input_file = sys.argv[1]
    words = sys.argv[2:]

    file_word_counter = FileWordCounter(input_file)

    for word in words:
        print(f"{word},{file_word_counter.get_word_count(word)}")
