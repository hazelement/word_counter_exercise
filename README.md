

# Programming Exercise

## Description

### Question

Given a comma seperated list of words in a single file, return the number of times the word was seen. 

The input will be in the form of a text file.

### Example input

`green,green,red,green,red`

### Expected output

```
green,3
red,2
```

## Input Assumptions


1. leading and trailing "," is ignored, ",," is ignored
2. word length is not checked. max word length is python array size limit.
    536870912 on a 32 bit system
3. all characters are assumed ascii characters

## Requirement

python3.6 and above

To check python version:
 
```bash
$ python --version
Python 3.7.1
```


## Usage

From project root directory, 

`$ python count_word.py input_file word1 word2 ...`

Example:

```bash
$ python count_word.py tests/data/case1.in ab bc
ab,2
bc,2

$ python count_word.py tests/data/case1.in ab bc f
ab,2
bc,2
f,0
```

## Tests

To run test, issue folowing command from project directory

```bash
$ python -m unittest discover tests
......
----------------------------------------------------------------------
Ran 6 tests in 0.007s

OK

```

To add more test cases, refer to existing test files in `tests/data`.

Each test case consists of 2 files, `*.in` and `*.cmp`. The two file names must match.

1. `*.in` is input file with only one line in the file, for example `green,green,red,red`.
2. `*.cmp` is the truth file for comparison, each line is a word and its occurance seperated by comma.

  
