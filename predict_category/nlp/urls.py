import os

DIR_PATH = os.path.dirname(os.path.realpath(__file__))
PARENT_PATH = os.path.abspath(os.path.join(DIR_PATH, os.pardir))
DICTIONARY_PATH = os.path.join(PARENT_PATH, "dictionary")
STOP_WORDS = os.path.join(DICTIONARY_PATH, "stop_words3.txt")
print(STOP_WORDS)