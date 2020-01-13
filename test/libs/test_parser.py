#! /usr/bin/env python3
# coding: utf-8

# from pbapp import app
# from unittest import TestCase
# from unittest.mock import Mock

import unittest

from pbapp.libs.parser import Parser


class ParserTest(unittest.TestCase):
    def setUp(self):
        """ Attention forme liste json pour le premier message !"""
        message = [{"message": "Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?"}]
        self.message = message[0]['message']
        self.parser = Parser(self.message)

    def test_list_stop_words(self):
        num_token_1 = len(self.message)

        self.assertEqual(num_token_1, 1, "User write a request")

    def test_normalisation(self):
        exist = 0
        self.mes_test = self.parser.normalisation()
        for w in self.mes_test:
            if w == "!":
                exist = 1

        # si stopword exist =! 1
        self.assertNotEqual(exist, 1, "La ponctuation à été supprimé")

    def test_suppr_stop_words(self):
        self.mes_test = self.parser.list_stop_words()
        exist = 0
        for w in self.mes_test:
            if w == "grandpy":
                exist = 1

        self.assertNotEqual(exist, 0, "Les stop_words sont bien supprimmé")


if __name__ == '__main__':
    unittest.main()
