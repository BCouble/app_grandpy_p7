#! /usr/bin/env python3
# coding: utf-8

import unittest

from pbapp.libs.parser import Parser


class ParserTest(unittest.TestCase):
    def setUp(self):
        self.message = "Hey GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?"
        self.parser = Parser(self.message)

    def test_split_message(self):
        mes_split = self.parser.split_message()
        print(self.parser.message_recive)
        self.assertEqual(self.parser.split_message(), ['Hey', 'GrandPy', '!', 'Est-ce', 'que', 'tu', 'connais', "l'adresse", "d'OpenClassrooms", '?'])

    def test_upper(self):

        self.assertEqual(self.parser.lowercase_message(), "hey grandpy ! est-ce que tu connais l'adresse d'openclassrooms ?")

    def test_remove_punct_blank(self):

        self.assertEqual(self.parser.remove_punct_blank(), "Hey GrandPy   Est ce que tu connais l adresse d'OpenClassrooms")

    def test_remove_stop_words(self):
        self.mes_test = self.parser.remove_stop_words()
        exist = 0
        for w in self.mes_test:
            if w == "grandpy":
                exist = 1

        self.assertNotEqual(exist, 0, "Les stop_words sont bien supprimmé")


if __name__ == '__main__':
    unittest.main()
