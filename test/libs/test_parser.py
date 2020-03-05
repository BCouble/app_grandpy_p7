#! /usr/bin/env python3
# coding: utf-8

import unittest

from pbapp.libs.parser import Parser


class ParserTest(unittest.TestCase):
    def setUp(self):
        self.message = "Hey GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?"
        self.parser = Parser(self.message)

    def test_split_message(self):
        """ Ici nous vérifions si la phrase est bien séparée """

        self.assertEqual(self.parser.split_message_with_ponc(),
                         ['', 'Hey', 'GrandPy', 'Est', 'ce', 'que', 'tu', 'connais', 'l', 'adresse', 'd',
                          'OpenClassrooms'])

    def test_upper(self):
        """ Ici nous vérifions si le texte est en minuscule """
        self.parser.split_message_with_ponc()

        self.assertEqual(self.parser.lowercase_message(),
                         ['', 'hey', 'grandpy', 'est', 'ce', 'que', 'tu', 'connais', 'l', 'adresse', 'd',
                          'openclassrooms'])

    def test_remove_punct_blank(self):
        """ Ici nous vérifions si il reste des symbole de ponctuation """
        self.parser.split_message_with_ponc()
        self.parser.lowercase_message()

        self.assertEqual(self.parser.remove_punct_blank(),
                         ['', 'hey', 'grandpy', 'est', 'ce', 'que', 'tu', 'connais', 'l', 'adresse', 'd',
                          'openclassrooms'])

    def test_remove_stop_words(self):
        """ Ici nous vérifions si les stop words ont été supprimées """
        self.parser.split_message_with_ponc()
        self.parser.lowercase_message()
        self.parser.remove_punct_blank()

        self.assertEqual(self.parser.remove_stop_words(), ' openclassrooms')


if __name__ == '__main__':
    unittest.main()
