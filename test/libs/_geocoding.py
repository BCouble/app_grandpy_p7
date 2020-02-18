#! /usr/bin/env python3
# coding: utf-8

import unittest
from pbapp.libs.geocoding import Geocode
from unittest.mock import Mock
from unittest import TestCase


class TestGeocodingAPI(TestCase):

    def setUp(self):

        geocode_response = {
            "result": [{
                {"formatted_address"}: "Paris, France",
                "geometry": {
                    "location": {
                        "lat": 48.856614,
                        "lng": 2.3522219,
                    },
                },
                "viewport": {
                    "northeast": {
                        "lat": 48.9021449,
                        'lng': 2.4699208,
                    },
                    "southwest": {
                        'lat': 48.815573,
                        'lng': 2.224199,
                    },
                },
                "id": "691b237b0322f28988f3ce03e321ff72a12167fd",
                "name": "Paris",
                "place_id": "ChIJD7fiBh9u5kcRYJSMaMOCCwQ",
            }],
            "status": "OK"
        }

        self.geocode = Geocode()
        self.geocode.search = Mock()
        self.geocode.search.return_value = geocode_response

    def test_search(self):
        """ Ici nous verifions si nous avons bien un retour de l'API"""
        pass

    def test_status(self):
        """ Ici nous vérifions l'état du status du retour de l'API"""
        self.assertEqual(self.geocode.status, "OK")

    def test_place_id(self):
        """ Ici nous vérifions la place ID """
        self.assertEqual(self.geocode.place_id, "ChIJD7fiBh9u5kcRYJSMaMOCCwQ")

    def test_address(self):
        """ Ici nous récupérons l'adresse formatée """
        self.assertEqual(self.geocode.address, "Paris, France")

    def test_coordinate(self):
        """ Ici nous récupérons la longitude et la latitude """
        self.assertEqual(self.geocode.coordinate, (48.856614, 2.3522219))

    def test_get_return(self):
        """ Ici nous vérifions l'état des information obtenue """
        pass


if __name__ == '__main__':
    unittest.main()