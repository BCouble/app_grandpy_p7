#! /usr/bin/env python3
# coding: utf-8

import unittest
import json
from pbapp.libs.json import Json
from unittest.mock import patch


class JsonfileTest(unittest.TestCase):
    def setUp(self):
        # open shemas's file
        self.jsonFile = Json()

    @patch('pbapp.Json.openShema')
    def test_open_JSON_shema_geocode(self, mock_open_json_file):
        # load mock
        mock_open_json_file.return_value = {

        }
        self.shema_geocode = self.jsonFile.open_json_shema(geocode)
        healthy_product = OpenFoodFactsAPI()
        self.assertEqual(healthy_product.count_product_numb("ferrero"), 2)
        pass

    @patch('pbapp.Json.compareShema')
    def test_valid_JSON_shema_geocode(self, mock_valid_json_file):
        # load mock
        mock_open_json_file.return_value = {

        }
        healthy_product = OpenFoodFactsAPI()
        healthy_product._get_product_from_api = Mock()
        healthy_product._get_product_from_api.return_value = api_response
        pass
        validate(self.shema_geocode, mock_shema_geocode)

    @patch('pbapp.Json.openShema')
    def test_open_JSON_shema_wikimedia(self):
        self.shema_wikimedia = self.jsonFile.open_json_shema(wikimedia)
        pass

    @patch('pbapp.Json.compareShema')
    def test_valid_JSON_shema_wikimedia(self):
        # load mock
        wikimedia_response = {

        }
        pass
        #with self.assertRaisesRegex(ValidationError, msg):
         #   validate(self.shema_wikimedia, mock_shema_wikimedia)


if __name__ == '__main__':
    unittest.main()