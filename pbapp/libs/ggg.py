#! /usr/bin/env python3
# coding: utf-8
import requests
from pbapp.key import key


class Geocode:

    def __init__(self):
        self.key_api = key
        self.search_url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
        self.details_url = "https://maps.googleapis.com/maps/api/place/details/json"
        self.return_result = []

    def search(self, query):
        search_payload = {"key": key, "query": query}
        search_req = requests.get(self.search_url, params=search_payload)
        search_json = search_req.json()

        return search_json

    def place_id_status(self, search):
        place_id = search["results"][0]["place_id"]

        self.return_result.append(place_id)

    def address(self, search):
        address_format = search["result"]["formatted_address"]

        self.return_result.append(address_format)

    def coordinate(self, search):
        lat = search["result"]["geometry"]["location"]["lat"]
        lng = search["result"]["geometry"]["location"]["lng"]

        self.return_result.append(lat, lng)

    def verification(self):
        try:
            if data["results"][0]["geometry"]["location_type"] != "APPROXIMATE":
                location_info["address"] = data["results"][0]["formatted_address"]
                location_info["latitude"] = data["results"][0]["geometry"]["location"]["lat"]
                location_info["longitude"] = data["results"][0]["geometry"]["location"]["lng"]
                location_info["status"] = "FOUND"
            else:
                raise KeyError
        except KeyError:
            location_info["status"] = "NOT_FOUND"
        except:
            location_info["status"] = "REQUEST_PROBLEM"

        return location_info
