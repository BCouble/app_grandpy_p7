#! /usr/bin/env python3
# coding: utf-8
import os
import unittest
from pbapp.libs.geocoding import Geocode
from pbapp.libs.json import Json
from unittest.mock import patch


class JsonfileTest(unittest.TestCase):
    def setUp(self):
        # open shemas's file
        self.jsonFile = Json()
        self.shema_geocode = os.path.isfile("./pbapp/static/json/shemas/geocode.json")
        self.api_response = {

        }

    def test_find_JSON_shema_geocode(self):

        self.assertTrue(self.shema_geocode)

    @patch('pbapp.Json.open_json_shema')
    def test_valide_JSON_shema_geocode(self, mock_open_json_file):
        # load mock
        mock_open_json_file.return_value = {
            "latitude": 48.801408,
            "longitude": 2.130122,
            "address": "78000 Versailles, France",
            "place_id": "ChIJvSD0dbR95kcRukqEDa0AnoY",
            "status": "OK"
        }
        self.shema_geocode = self.jsonFile.open_json_shema(geocode)
        api_geocode = Geocode()


if __name__ == '__main__':
    unittest.main()