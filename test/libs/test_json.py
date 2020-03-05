#! /usr/bin/env python3
# coding: utf-8
import os
import unittest
from unittest import mock

from pbapp.libs.geocoding import Geocode
from pbapp.libs.json import Json
from unittest.mock import patch


class JsonfileTest(unittest.TestCase):

    def setUp(self):
        self.schema_geocode = Geocode()
        self.jsonFile = Json()

        # Replace `some_module.method` with a `mock.Mock`
        my_patch = mock.patch.object(Json, 'open_json_shema')
        my_patch.start()

        # When the test finishes running, put the original method back.
        self.addCleanup(my_patch.stop)

    def test_find_JSON_shema_geocode(self):

        self.assertTrue(self.shema_geocode)

    @patch('pbapp.Json.valid_json_shema')
    def test_valide_JSON_shema_geocode(self, mock_open_json_file):
        """ Ici nous vérifions le shema json pour geocode"""
        mock_open_json_file.return_value = {
            "html_attributions": [],
            "results": [{
                "formatted_address": "Paris, France",
                "geometry": {
                    "location": {
                        "lat": 48.856614,
                        "lng": 2.3522219
                    }
                },
                "viewport": {
                    "northeast": {
                        "lat": 48.9021449,
                        "lng": 2.4699208
                    },
                    "southwest": {
                        "lat": 48.815573,
                        "lng": 2.224199
                    }
                },
                "id": "691b237b0322f28988f3ce03e321ff72a12167fd",
                "name": "Paris",
                "place_id": "691b237b0322f28988f3ce03e321ff72a12167fd"
            }],
            "status": "OK"
        }
        self.shema_geocode = self.jsonFile.open_json_shema(self.shema_geocode)
        valid_shema = self.jsonFile.valide_json_shema()
        self.assertTrue(valid_shema)
        self.assertIsInstance(valeur !, int)


if __name__ == '__main__':
    unittest.main()