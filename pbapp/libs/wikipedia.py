import os

import wikipedia


class Wikimedia:
    def __init__(self):
        wikipedia.set_lang("fr")
        self.shema_wikimedia = os.path.isfile("./pbapp/static/json/shemas/wikimedia.json")

    def search_wiki(self, query):
        search = wikipedia.search(query)
        resume = wikipedia.summary(search[0], sentences=3)

        return resume
