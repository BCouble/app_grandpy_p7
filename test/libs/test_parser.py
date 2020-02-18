#! /usr/bin/env python3
# coding: utf-8

import unittest

from pbapp.libs.parser import Parser


class ParserTest(unittest.TestCase):
    def setUp(self):
        self.message_findall = ['', 'Hey', 'GrandPy', 'Est', 'ce', 'que', 'tu', 'connais', 'l', 'adresse', 'd',
                                'OpenClassrooms']
        self.parser = Parser(self.message_findall)

    def test_split_message(self):
        message = "Hey GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?"
        parser = Parser(message)
        sp_parser = parser.split_message_with_ponc()

        self.assertEqual(sp_parser,
                         ['', 'Hey', 'GrandPy', 'Est', 'ce', 'que', 'tu', 'connais', 'l', 'adresse', 'd',
                          'OpenClassrooms'])

    def test_upper(self):
        lo_parser = self.parser.lowercase_message()

        self.assertEqual(lo_parser,
                         ['', 'hey', 'grandpy', 'est', 'ce', 'que', 'tu', 'connais', 'l', 'adresse', 'd',
                          'openclassrooms'])

    def test_remove_punct_blank(self):
        r_p_blank = self.parser.remove_punct_blank()

        self.assertEqual(r_p_blank,
                         ['', 'Hey', 'GrandPy', 'Est', 'ce', 'que', 'tu', 'connais', 'l', 'adresse', 'd',
                          'OpenClassrooms'])

    def test_remove_stop_words(self):
        r_sw = self.parser.remove_stop_words()

        self.assertEqual(r_sw,
                         "-OpenClassrooms")


if __name__ == '__main__':
    unittest.main()
