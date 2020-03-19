#! /usr/bin/env python3
# coding: utf-8
import os

import requests
from pbapp.key import key


class Geocode:

    def __init__(self):
        self.key_api = key
        self.search_url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
        self.details_url = "https://maps.googleapis.com/maps/api/place/details/json"
        self.search_result = []
        self.return_result = []

    def search(self, query):
        search_payload = {"key": key, "query": query}
        search_req = requests.get(self.search_url, params=search_payload)
        search_json = search_req.json()
        self.search_result = search_json

        return search_json

    def status(self, search_result):
        status = search_result["status"]
        self.return_result.append(status)

        return status

    def place_id(self, search_result):
        place_id = search_result["results"][0]["place_id"]
        self.return_result.append(place_id)

        return place_id

    def address(self, search_result):
        address_format = search_result["results"][0]["formatted_address"]
        self.return_result.append(address_format)

        return address_format

    def coordinate(self, search_result):
        lat = search_result["results"][0]["geometry"]["location"]["lat"]
        lng = search_result["results"][0]["geometry"]["location"]["lng"]

        self.return_result.extend((lat, lng))

    def get_return(self):

        return self.return_result

