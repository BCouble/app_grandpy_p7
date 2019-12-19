# ! /usr/bin/env python3
# coding: utf-8
"""
Project 5
App Pur beurre
"""
from pbapp.libs.parser import Parser
from pbapp.libs.geocoding import Geocode
from pbapp.libs.wikipedia import Wikimedia


def write_message():
    message = input("ici quest :")

    return message


def load_parser(message):
    parser = Parser(message)
    parser.normalisation()
    parser.list_stop_words()
    query = parser.suppr_sw()

    print("query : ")
    print(query)


    # query = "openclassroom"

    return query


def quest_geocode(query):
    geocode = Geocode()
    map_geo = geocode.search(query)
    geocode.status()
    geocode.place_id()
    geocode.address()
    geocode.coordinate()

    return map_geo


def quest_wiki(query):
    wiki = Wikimedia()
    wiki.search_wiki(query)


def main():
    quest = load_parser(message=write_message())
    quest_geocode(quest)
    quest_wiki(quest)


if __name__ == "__main__":
    main()
