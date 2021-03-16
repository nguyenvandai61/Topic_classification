import os
import json
import predict_category.predict_models.settings
import pickle
import nltk.data
class FileReader(object):
    def __init__(self, filePath, encoder = None):
        self.filePath = filePath
        self.encoder = encoder if encoder != None else 'utf-8'
    
    def read(self):
        with open(self.filePath, 'r') as f:
            s = f.read()
        return s
    
    def content(self):
        s = self.read()
        return s.decode(self.encoder)
    
    def read_json(self):
        s = ''
        with open(self.filePath, 'r', encoding=self.encoder) as f:
            s = json.load(f)
        return s

    def read_stopwords(self):
        with open(self.filePath, 'r', encoding="utf-8") as f:
            stopwords = set([w.strip().replace(' ', '_') for w in f.readlines()])
        return stopwords

    def load_dictionary(self):
        return corpora.Dictionary.load_from_text(self.filePath)
class FileStore(object):
    def __init__(self, filePath, data = None):
        self.filePath = filePath
        self.data = data

    def store_json(self):
        with open(self.filePath, 'w') as outfile:
            json.dump(self.data, outfile)

    def store_dictionary(self, dict_words):
        dictionary = corpora.Dictionary(dict_words)
        dictionary.filter_extremes(no_below=20, no_above=0.3)
        dictionary.save_as_text(self.filePath)
    
    def save_pickle(self, obj):
        outfile = open(self.filePath, 'wb')
        fastPickler = pickle.Pickler(outfile, pickle.HIGHEST_PROTOCOL)
        fastPickler.fast = 1
        fastPickler.dump(obj)
        outfile.close()
from pyvi import ViTokenizer, ViPosTagger
import numpy as np
import string
import re


class NLP(object):
    def __init__(self, text=None):
        self.text = text
        self.stopwords = FileReader("predict_category/predict_models/stop_words3.txt").read_stopwords()
        # print(str(len(self.stopwords)))
        self.newWords = []
        
    def remove_tags(self, raw_html):
        cleanr = re.compile('<.*?>')
        cleantext = re.sub(cleanr, '', raw_html )
        return cleantext

    def remove_links(self, text):
        text = re.sub(r'^https?:\/\/.*[\r\n]*', '', text, flags=re.MULTILINE)
        return text

    def remove_punctuation(self, text):
        return text.translate(str.maketrans('', '', string.punctuation))
        

    def remove_stopwords(self, words, stopwords):
        important_words = []
        for index in range(len(words)):
            if (words[index] not in stopwords ):
                important_words.append(words[index])
        self.tokens = important_words
        return important_words
    
    def lower_sentences(self, text):
         return text.lower()

    def tokenize_sentences(self, text):
        return ViTokenizer.tokenize(text)

    def segment_word(self, tokens):
        return ViPosTagger.postagging(tokens)
    
    def keep_verb_noun(self, postags):
        res = []
        for index in range(len(postags[0])):
            if postags[1][index] == 'N' or postags[1][index] == 'V':
                res.append(postags[0][index])
        return res

    def remove_digits(self, tokens):
        new_words = []
        for index in range(len(tokens)):
            if not tokens[index].isdigit():
                new_words.append(tokens[index])
        return new_words
    
    def count_tokens(self, tokens):
        unique, counts = np.unique(tokens, return_counts=True)
        return dict(zip(unique, counts))
    
    def retrieve_tokens_times(self, tokens, n):
        tokens = {k: v for k, v in self.count_tokens(tokens).items() if int(v) >= n}
        return tokens 
        
    def preprocessText(self, text ):
        processed_text = text
        processed_text = self.remove_tags(processed_text)
        processed_text = self.lower_sentences(processed_text)
        processed_text = self.remove_links(processed_text)
        processed_text = self.remove_punctuation(processed_text)
        tokens = self.tokenize_sentences(processed_text)
        tokens = self.segment_word(tokens)
        # print(tokens)
        tokens = self.keep_verb_noun(tokens)
        important_tokens = self.remove_stopwords(tokens, self.stopwords)
        important_tokens = self.remove_digits(important_tokens)
        important_tokens = self.retrieve_tokens_times(important_tokens, 3)
        self.tokens = important_tokens
        return self.tokens

    def __repr__(self):
        return self.text