#! /usr/bin/env python3
# coding: utf-8
import nltk
from nltk.corpus import stopwords
from nltk.stem.snowball import FrenchStemmer
from nltk.chunk import conlltags2tree, tree2conlltags
from pprint import pprint
from pbapp.constant import STOPWORDS

#import spacy
#from spacy import displacy
#from collections import Counter
#import en_core_web_sm
#nlp = en_core_web_sm.load()

textt = [{"message": "Dans notre cas, je voulais étudier la richesse du vocabulaire des artistes."}]
text = [{"message": "Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?"}]
message = text[0]['message']
# print(message)
tokenizer = nltk.RegexpTokenizer(r'\w+')
# message = tokenizer.tokenize(message.lower())
# print(message)
sw = []
list_sw_1 = set(stopwords.words('french'))
sw.append(list_sw_1)
# print(list_sw_1)
list_sw_2 = STOPWORDS
sw.append(list_sw_2)
# print(sw)

for w in list_sw_1:
    list_sw_2.append(w)

# list_test = list_sw_1 + list_sw_2
# print(list_test)

# print(list_sw_2)


message = tokenizer.tokenize(message.lower())
print(message)
# message_parser = nltk.word_tokenize(message)
# print(message_parser)

stemmer = FrenchStemmer()

select = []
# sel = []
for w in message:
    print(w)
    stemmer.stem(w)
    print(w)
    if w in list_sw_2:
        pass
        # sel.append(w)
    else:
        select.append(w)

# print(sel)
print(select)

stemmed_words = []  # declare an empty list to hold our stemmed words
stemmer = FrenchStemmer()  # create a stemmer object in the FrenchStemmer class
for w in select:
    stemmed_word = stemmer.stem(w)  # stem the word
    stemmed_words.append(stemmed_word)  # add it to our stemmed word list
stemmed_words.sort()  # sort the stemmed_words

print(stemmed_words)

ex = 'European authorities fined Google a record $5.1 billion on Wednesday for abusing its power in the mobile phone market and ordered the company to alter its practices'


def preprocess(sent):
    sent = nltk.word_tokenize(sent)
    sent = nltk.pos_tag(sent)
    return sent


sent = preprocess(ex)
print(sent)
pattern = 'NP: {<DT>?<JJ>*<NN>}'
cp = nltk.RegexpParser(pattern)
cs = cp.parse(sent)
print(cs)
iob_tagged = tree2conlltags(cs)
pprint(iob_tagged)

doc = nlp('European authorities fined Google a record $5.1 billion on Wednesday for abusing its power in the mobile phone market and ordered the company to alter its practices')
pprint([(X.text, X.label_) for X in doc.ents])
