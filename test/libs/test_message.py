#! /usr/bin/env python3
# coding: utf-8

import unittest
from pbapp.libs.message import Message
from unittest.mock import Mock
from unittest import TestCase


class TestMessagePapyBOT(TestCase):

    def setUp(self):
        message_response_geocode = {
            "OK": "Indique qu'aucune erreur ne s'est produite ; l'adresse a été analysée avec succès et au moins un "
                  "géocode a été renvoyé.",
            "ZERO_RESULTS": "Indique que le géocode a été analysé avec succès mais n'a pas renvoyé de résultats. Cela "
                            "peut se produire si le géocode a été transmis à une adresse inexistante.",
            "OVER_DAILY_LIMIT": "Indique un des éléments suivants : La clé API est manquante ou non valide, "
                                "facturation inactive sur votre compte, Un plafond que vous vous êtes imposé a été "
                                "dépassé, Le mode de paiement non valide",
            "OVER_QUERY_LIMIT": "Indique que vous avez dépassé votre quota.",
            "REQUEST_DENIED": "Indique que votre demande a été refusée.",
            "INVALID_REQUEST": "Indique généralement que la requête (adresse, composants ou latlng) est manquante.",
            "UNKNOWN_ERROR": "Indique que la demande n'a pas pu être traitée en raison d'une erreur du serveur. La "
                             "requête peut réussir si vous essayez à nouveau. "
        }

        self.message = Message()
        self.message.search = Mock(return_value=message_response_geocode)

    def test_message_home(self):
        """ Ici nous verifions que le message est bien un string """
        pass

    def test_message_error_geocode(self):
        """ Ici nous vérifions le message d'erreur de geocode """
        pass

    def test_message_error_wikimedia(self):
        """ Ici nous vérifions le message d'erreur de wikimedia """
        pass

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
