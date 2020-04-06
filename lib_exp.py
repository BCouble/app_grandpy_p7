# ! /usr/bin/env python3
# coding: utf-8
"""
Project 7
"""
from pbapp.libs.geocoding import Geocode
from pbapp.libs.parser import Parser
from pbapp.libs.wikipedia import Wikimedia


def write_message():
    message = input("ici quest :")

    return message


def load_parser(message):
    list_parse = []
    parser = Parser(message)
    one = parser.split_message_with_ponc()
    list_parse.append(one)
    tow = parser.lowercase_message()
    list_parse.append(tow)
    tree = parser.remove_punct_blank()
    list_parse.append(tree)
    m_parser = parser.remove_stop_words()
    foor = m_parser
    list_parse.append(foor)
    #print(m_parser)

    return list_parse


def quest_geocode(query):
    message_geocode = {}
    geocode = Geocode()
    map_geo = geocode.search(query)
    geocode.status(map_geo)
    geocode.place_id(map_geo)
    geocode.address(map_geo)
    gmap = geocode.coordinate(map_geo)

    return map_geo, gmap


def quest_wiki(query):
    wiki = Wikimedia()
    r_wiki = wiki.search_wiki(query)
    #print(r_wiki)

    return r_wiki


def main():
    quest = load_parser(message=write_message())
    quest_geocode(quest)
    quest_wiki(quest)


if __name__ == "__main__":
    main()
