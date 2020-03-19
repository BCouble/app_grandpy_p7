#! /usr/bin/env python3
# coding: utf-8

import unittest
from pbapp.libs.geocoding import Geocode
from pbapp.libs.json import Json
from unittest.mock import Mock
from unittest import TestCase


class TestGeocodingAPI(TestCase):

    def setUp(self):
        # Json Mock geocode API
        geocode_response = {
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
        # Load geocoding
        self.geocode = Geocode()
        # Load json
        self.jsonFile = Json()
        # Load schema
        file = "geocode"
        self.schema_geocode = self.jsonFile.open_json_shema(file)
        # Mock data geocode_response
        self.geocode.search = Mock(return_value=geocode_response)
        # Load return API avec query Paris
        query = "Bonjour Grandpy, j'aimerais visiter Paris"
        self.return_json_api_geocode = self.geocode.search(query)

    def test_open_json_schema_geocode(self):
        """ Open the json schema of the Mock """

        self.assertTrue(self.schema_geocode)

    def test_json_schema_mock(self):
        """ Validate the json schema of the Mock """

        self.assertDictEqual(self.jsonFile.valide_json_shema(self.return_json_api_geocode, self.schema_geocode))

    def test_status(self):
        """ Mock geocode_response return status """

        self.assertEqual(self.geocode.search.return_value["status"], "OK")

    def test_place_id(self):
        """ Mock geocode_response return place_id """

        self.assertEqual(self.geocode.search.return_value["results"][0]["place_id"],
                         "691b237b0322f28988f3ce03e321ff72a12167fd")

    def test_address(self):
        """ Mock geocode_response return formatted_address """

        self.assertEqual(self.geocode.search.return_value["results"][0]["formatted_address"], "Paris, France")

    def test_coordinate(self):
        """ Mock geocode_response return lat, lng """

        self.assertEqual(self.geocode.search.return_value["results"][0]["geometry"]["location"]["lat"], 48.856614)
        self.assertEqual(self.geocode.search.return_value["results"][0]["geometry"]["location"]["lng"], 2.3522219)

    def test_get_return(self):
        """ Check list returned by geocode """
        # charger var reponse test schema
        # valid shema mock
        #
        # test inte api
        return_list = ['OK', '691b237b0322f28988f3ce03e321ff72a12167fd', 'Paris, France', 48.856614, 2.3522219]
        self.geocode.status(self.return_json_api_geocode)
        self.geocode.place_id(self.return_json_api_geocode)
        self.geocode.address(self.return_json_api_geocode)
        self.geocode.coordinate(self.return_json_api_geocode)
        map_geo = self.geocode.get_return()

        self.assertListEqual(map_geo, return_list)


if __name__ == '__main__':
    unittest.main()
