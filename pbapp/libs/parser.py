#! /usr/bin/env python3
# coding: utf-8


import nltk
from nltk.corpus import stopwords
from nltk.stem.snowball import FrenchStemmer

from pbapp.constant import STOPWORDS


class Parser:
    def __init__(self, message):
        print(message)
        self.message_recive = message
        self.sw = []

    def list_stop_words(self):
        list_sw = STOPWORDS
        list_sw_2 = set(stopwords.words('french'))
        list_sw.append(list_sw_2)

        self.sw = list_sw

    def normalisation(self):
        tokenizer = nltk.RegexpTokenizer(r'\w+')

        self.message_recive = tokenizer.tokenize(self.message_recive.lower())
        print("Normalisation : ")
        print(self.message_recive)

    def suppr_sw(self):
        # Bibliotheque nltk stopword
        select = []
        for w in self.message_recive:
            if w in self.sw:
                pass
            else:
                select.append(w)
        select = "-".join(select)
        return select
