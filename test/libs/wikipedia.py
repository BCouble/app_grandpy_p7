#! /usr/bin/env python3
# coding: utf-8


import unittest
from pbapp.libs.geocoding import Geocode
from unittest.mock import Mock
from unittest import TestCase


class Wikimedia:
    def __init__(self):
        wikipedia.set_lang("fr")

    def search_wiki(self, query):
        search = wikipedia.search(query)
        print(search)
        print(wikipedia.summary(search[0], sentences=3))

        return search
