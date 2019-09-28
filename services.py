from abc import ABC, abstractmethod


class CharacterStreamConsumer(ABC):

    @abstractmethod
    def push(self, character):
        """
        Receives a character from stream
        :param character: string with length 1
        """
        pass

    @abstractmethod
    def flush(self):
        """flush buffer content"""
        pass


class WordCounter(ABC):

    @abstractmethod
    def get_word_count(self, word):
        """
        Get count for given word
        :param word: string
        :return: number of times this word seens
        """
        pass


class CharacterToWordParser(CharacterStreamConsumer):
    """
    A char stream to word parser
    """

    def __init__(self, stop_char=','):
        """
        :param stop_char: stop char that seperates words, default ','
        """
        self.buffer = ""
        self.stop_char = ','

    def push(self, character):
        """
        Receiver a character to buffer and return buffered characters as a word if this character is ","
        else return None
        :param character: string with length 1
        :return: None or word as string
        """
        word = None
        if character == self.stop_char:
            word = self.buffer
            self.buffer = ''
        else:
            self.buffer += character
        return word if word != '' else None

    def flush(self):
        """ flush character in buffer and return all characters as a word
        if buffer is empty, return None
        :return: None or word
        """
        word = self.buffer
        self.buffer = ''
        return word if word != '' else None


class WordStreamCounter(CharacterStreamConsumer, WordCounter):
    """
    Count words from char stream
    """

    def __init__(self):
        self.library = dict()
        self.character_parser = CharacterToWordParser()

    def _add_word_to_library(self, word):
        if word is not None:
            # add word to library
            if word not in self.library:
                self.library[word] = 0
            self.library[word] += 1

    def push(self, character):
        # parse character into word
        word = self.character_parser.push(character)
        self._add_word_to_library(word)

    def flush(self):
        word = self.character_parser.flush()
        self._add_word_to_library(word)

    def get_word_count(self, word):
        return self.library[word] if word in self.library else 0


class FileWordCounter(WordCounter):

    def __init__(self, filename):
        self.filename = filename
        self.word_stream_counter = WordStreamCounter()
        self._parse_file(filename)

    def _parse_file(self, filename):
        with open(filename, 'r') as f:
            line = f.read()
            line.strip('\n')  # remove line break
            for c in line:
                self.word_stream_counter.push(c)
            self.word_stream_counter.flush()

    def get_word_count(self, word):
        return self.word_stream_counter.get_word_count(word)
