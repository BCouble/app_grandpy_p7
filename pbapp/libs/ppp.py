#! /usr/bin/env python3
# coding: utf-8

text = [{"message": "Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?"}]


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

    def stem_words(self):
        '''stems the word list using the French Stemmer'''
        # stemming words
        stemmed_words = []  # declare an empty list to hold our stemmed words
        stemmer = FrenchStemmer()  # create a stemmer object in the FrenchStemmer class
        for w in self.message_recive:
            stemmed_word = stemmer.stem(w)  # stem the word
            #print(w)
            #print(stemmed_word)
            if w == stemmed_word:
                stemmed_words.append(stemmed_word)  # add it to our stemmed word list
        stemmed_words.sort()  # sort the stemmed_words
        print("stemmed xords : ")
        print(stemmed_words)
        return stemmed_words

