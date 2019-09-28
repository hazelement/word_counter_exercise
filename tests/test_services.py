import unittest
import os
from services import CharacterToWordParser, WordStreamCounter, FileWordCounter


class CharacterToWordParserTestCase(unittest.TestCase):

    def setUp(self):

        self.word_parser = CharacterToWordParser()

    def test_string_parsing(self):

        test_string = 'ab,bc,cd,ab,bc,de'

        res = []
        for c in test_string:
            w = self.word_parser.push(c)
            if w is not None:
                res.append(w)
        w = self.word_parser.flush()
        if w is not None:
            res.append(w)

        self.assertEqual(','.join(res), test_string, "parsed word list doesn't match input string")

    def test_push_action(self):
        w = self.word_parser.push("a")
        self.assertIsNone(w, f'{w} is not None')

        w = self.word_parser.push("a")
        self.assertIsNone(w, f'{w} is not None')

        w = self.word_parser.push(",")
        self.assertEqual(w, 'aa', f"returned word {w} doesn't match 'aa'")

    def test_flush_action(self):
        w = self.word_parser.push("a")
        self.assertIsNone(w, f'{w} is not None')

        w = self.word_parser.push("a")
        self.assertIsNone(w, f'{w} is not None')

        w = self.word_parser.flush()
        self.assertEqual(w, 'aa', f"flushed word {w} doesn't match 'aa'")

class WordStreamCounterTestCase(unittest.TestCase):

    def setUp(self):
        self.word_counter = WordStreamCounter()

    def test_word_stream_counter(self):
        test_string = 'ab,bc,cd,ab,bc,de'

        for c in test_string:
            self.word_counter.push(c)
        self.word_counter.flush()

        self.assertEqual(self.word_counter.get_word_count('ab'), 2)
        self.assertEqual(self.word_counter.get_word_count('bc'), 2)
        self.assertEqual(self.word_counter.get_word_count('cd'), 1)
        self.assertEqual(self.word_counter.get_word_count('de'), 1)
        self.assertEqual(self.word_counter.get_word_count('not exist'), 0)

    def test_weired_inputs(self):
        test_string = ',ab,bc,,,,cd,ab,bc,de,'

        for c in test_string:
            self.word_counter.push(c)

        # ,, is considered as empty word ''
        # trailing , is ignored instead of considering as an empty word at end
        self.assertEqual(self.word_counter.get_word_count(''), 0)
        self.assertEqual(self.word_counter.get_word_count('ab'), 2)


class FileWordCounterTestCase(unittest.TestCase):

    def _parse_cmp_file(self, filename):

        cmp_reference = dict()
        with open(filename, 'r') as f:
            line = f.readline()
            while line:
                line.strip('\n')
                word, count = line.split(',')
                cmp_reference[word] = int(count)
                line = f.readline()
        return cmp_reference


    def test_all_cases(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        data_dir = os.path.join(dir_path, 'data')
        test_cases = ['case1']

        for test_case in test_cases:
            input_file = os.path.join(data_dir, test_case+'.in')
            output_file = os.path.join(data_dir, test_case+'.cmp')

            file_word_counter = FileWordCounter(input_file)
            truth = self._parse_cmp_file(output_file)

            for k, v in truth.items():
                self.assertEqual(file_word_counter.get_word_count(k), truth[k])






