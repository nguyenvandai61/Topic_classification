import os

DIR_PATH = os.path.dirname(os.path.realpath(__file__))
PARENT_PATH = os.path.abspath(os.path.join(DIR_PATH, os.pardir))

DICTIONARY_PATH = os.path.join(PARENT_PATH, "dictionary")
STOP_WORDS = os.path.join(DICTIONARY_PATH, "stop_words3.txt")

RAW_DATA_PATH = os.path.join(PARENT_PATH, "raw_data")
RAW_DATA_TEST_PATH = os.path.join(RAW_DATA_PATH, "test")


EXAM1 = os.path.join(RAW_DATA_TEST_PATH, "example1.txt")

print(STOP_WORDS)
print(EXAM1)