#! /usr/bin/env python3
# coding: utf-8

import json
import os

from jsonschema import validate


class Json:

    def __inti__(self):
        self.shema_geocode = os.path.isfile("./pbapp/static/json/shemas/geocode.json")

    def open_json_shema(self, file):
        """ Load schema json """
        link = "./pbapp/static/json/shemas/" + file + ".json"
        with open(link) as schema_file:
            schema_json = json.load(schema_file)
        schema_file.close()

        return schema_json

    def valide_json_shema(self, schema_to_test, schema_valid):
        try:
            validate(schema_to_test, schema_valid)
        except Exception as valid_err:
            print("Validation KO: {}".format(valid_err))
            raise valid_err
        else:
            # Realise votre travail
            print("Validé")
            valid = True
            return valid
