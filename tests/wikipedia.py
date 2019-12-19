#! /usr/bin/env python3
# coding: utf-8


import wikipedia


class Wikimedia:
    def __init__(self):
        wikipedia.set_lang("fr")

    def search_wiki(self, query):
        search = wikipedia.search(query)
        print(search)
        print(wikipedia.summary(search[0], sentences=3))

        return search
