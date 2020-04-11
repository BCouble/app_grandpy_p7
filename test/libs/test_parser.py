#! /usr/bin/env python3
# coding: utf-8

import unittest

from pbapp.libs.parser import Parser


class ParserTest(unittest.TestCase):
    def setUp(self):
        self.message = "Hey GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?"
        self.parser = Parser(self.message)

    def test_split_message(self):
        """ Here we check if the sentence is well separated """

        self.assertEqual(self.parser.split_message_with_ponc(),
                         ['Hey', 'GrandPy', '!', 'Est', 'ce', 'que', 'tu', 'connais', 'l', 'adresse', 'd', 'OpenClassrooms', '?'])

    def test_upper(self):
        """ Here we check if the text is in lower case """
        self.parser.split_message_with_ponc()

        self.assertEqual(self.parser.lowercase_message(),
                         ['hey', 'grandpy', '!', 'est', 'ce', 'que', 'tu', 'connais', 'l', 'adresse', 'd', 'openclassrooms', '?'])

    def test_remove_punct_blank(self):
        """ Here we check to see if there are any punctuation marks left """
        self.parser.split_message_with_ponc()
        self.parser.lowercase_message()

        self.assertEqual(self.parser.remove_punct_blank(),
                         ['hey', 'grandpy', '', 'est', 'ce', 'que', 'tu', 'connais', 'l', 'adresse', 'd', 'openclassrooms', ''])

    def test_remove_stop_words(self):
        """ Here we check if the stop words have been removed """
        self.parser.split_message_with_ponc()
        self.parser.lowercase_message()
        self.parser.remove_punct_blank()

        self.assertEqual(self.parser.remove_stop_words(), 'openclassrooms')


if __name__ == '__main__':
    unittest.main()
