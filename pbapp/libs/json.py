#! /usr/bin/env python3
# coding: utf-8

import json
import os

from jsonschema import validate


class Json:

    def __inti__(self):
        self.shema_geocode = os.path.isfile("./pbapp/static/json/shemas/geocode.json")

    def open_json_shema(self, file):
        """ Ici nous chargeons un schema json """
        with open(file) as schema_file:
            schema_json = json.load(schema_file)
        schema_file.close()

        return schema_json

    def valide_json_shema(self, file):
        pass
        try:
            validate(dict_to_test, dict_valid)
        except Exception as valid_err:
            print("Validation KO: {}".format(valid_err))
            raise valid_err
        else:
            # Realise votre travail
            valid = True
            return valid

