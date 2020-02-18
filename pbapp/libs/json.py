#! /usr/bin/env python3
# coding: utf-8

import json
from jsonschema import validate


class Json:

    def __inti__(self):
        pass

    def open_json_shema(self, file):
        pass
        with open(file) as schema_file:
            test_schema = json.load(schema_file)
        schema_file.close()

        return test_schema

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

