#! /usr/bin/env python3
# coding: utf-8


from unittest import TestCase
from pbapp.libs.wikipedia import Wikimedia


class TestWikimediaAPI(TestCase):
    def setUp(self):
        """ query for except """
        self.wikimedia = Wikimedia()

    def test_resume_search_wiki(self):
        """ check if a paragraph is returned """
        query = "openclassrooms"
        wiki_result = self.wikimedia.search_wiki(query)
        resume = "OpenClassrooms est un site web de formation en ligne qui propose à ses membres des cours " \
                 "certifiants et des parcours débouchant sur des métiers en croissance. Ses contenus sont réalisés en " \
                 "interne, par des écoles, des universités, des entreprises partenaires comme Microsoft ou IBM, " \
                 "ou historiquement par des bénévoles. Jusqu\'en 2018, n\'importe quel membre du site pouvait être " \
                 "auteur, via un outil nommé « interface de rédaction » puis « Course Lab »."

        self.assertEqual(resume, wiki_result)

    def test_except_search_wiki(self):
        """ check if except is raised """
        query = "????"
        wiki_result = self.wikimedia.search_wiki(query)
        resume = "Toutes mes excuses mon canari, mais les informations que j'avais sur ce lieu ont dû être formatées !"

        self.assertEqual(resume, wiki_result)
