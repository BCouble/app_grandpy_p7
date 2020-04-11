# ! /usr/bin/env python3
# coding: utf-8
"""
Project 7
"""
from pbapp.libs.geocoding import Geocode
from pbapp.libs.parser import Parser
from pbapp.libs.wikipedia import Wikimedia


def load_parser(message):
    parser = Parser(message)

    parser.split_message_with_ponc()
    parser.lowercase_message()
    parser.remove_punct_blank()
    m_parser = parser.remove_stop_words()

    return m_parser


def quest_geocode(query):
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

    return r_wiki
