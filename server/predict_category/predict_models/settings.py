import os

DIR_PATH = os.path.dirname(os.path.realpath(__file__))
DATA_TRAIN_PATH = os.path.join(DIR_PATH, 'train/')
DATA_TEST_PATH = os.path.join(DIR_PATH, 'test/')
DATA_TRAIN_JSON = os.path.join(DIR_PATH, 'data_train.json')
DATA_TEST_JSON = os.path.join(DIR_PATH, 'data_test.json')
DATA_RAW = os.path.join(DIR_PATH, 'raw_data/')
STOP_WORDS = os.path.join(DIR_PATH, 'stop_words3.txt')
SPECIAL_CHARACTER = '0123456789%@$.,=+-!;/()*"&^:#|\n\t\''
DICTIONARY_PATH = 'dictionary.txt'

# print(DATA_RAW)