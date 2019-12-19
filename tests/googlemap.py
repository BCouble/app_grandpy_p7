#! /usr/bin/env python3
# coding: utf-8


import unittest
print("google map")


class TestGmaps(unittest.TestCase):

    def setUp(self):
        # self.key_api = key_api
        self.results = [{
            "latitude": 48.801408,
            "longitude": 2.130122,
            "address": "78000 Versailles, France",
            "place_id": "ChIJvSD0dbR95kcRukqEDa0AnoY",
            "status": "OK"
        }]

    def test_json_return(self, monkeypatch):
        # blablz
        def mockreturn(request): # request
            return self.results

        monkeypatch.setattr(Gmaps, get_return, mockreturn)

        assert Gmaps.get_return["status"] == self.results[4]
        assert Gmaps.get_return["place_id"] == self.results[3]
        assert Gmaps.get_return["latitude"] == self.results[0]
        assert Gmaps.get_return["longitude"] == self.results[1]
        assert Gmaps.get_return["address"] == self.results[2]


if __name__ == '__main__':
    unittest.main()
