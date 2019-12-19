#! /usr/bin/env python3
# coding: utf-8

# from pbapp import app
# from unittest import TestCase
# from unittest.mock import Mock

import unittest
import nltk
from nltk.corpus import stopwords


class ParserTestCase(unittest.TestCase):

    def setUp(self):
        """ Attention forme liste json pour le premier message !"""
        text = [{"message": "Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?"}]
        self.text = text
        self.message = self.text[0]['message']
        # Découpage en mot : Tokenization
        tokenizer = nltk.RegexpTokenizer(r'\w+')
        self.norma = tokenizer.tokenize(self.message.lower())
        self.message_parser = nltk.word_tokenize(self.message)

    # 1 Récupération du corpus (le texte)
    def test_reciveText(self):
        # doit-être inférieure ou égale à 1, une phrase ;)
        num_token_1 = len(self.text)

        self.assertEqual(num_token_1, 1, "User write a request")

    # 2 Tokenization découpage en mots
    def test_parser(self):
        # Le nombre de mot doit-être supérieure ou égal à 3 :)
        num_token_2 = len(self.message_parser)
        self.assertIsNot(1, num_token_2, "GrandPy Découpe la phrase en mot ;)")

    # 3 Nettoyage passe 1
    def test_net_passe_one(self):
        # Bibliotheque nltk stopword
        stop_words = set(stopwords.words('french'))
        exist = 0
        fltr = []
        for w in self.message_parser:
            if w in stop_words:
                exist += 1
            else:
                fltr.append(w)

        # si stopword exist =! 1
        self.assertNotEqual(exist, 0, "Les stop_words sont bien détectés")

    # 4 Normalisation
    def test_normalisation(self):
        exist = 0
        for w in self.norma:
            if w == "!":
                exist = 1

        # si stopword exist =! 1
        self.assertNotEqual(exist, 1, "La ponctuation à été supprimé")

    # 5 stemming
    def test_stemming(self):
        # stemmer.stem(w)
        pass


if __name__ == '__main__':
    unittest.main()
