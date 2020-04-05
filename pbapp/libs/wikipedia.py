import os
import wikipedia


class Wikimedia:
    def __init__(self):
        wikipedia.set_lang("fr")
        self.shema_wikimedia = os.path.isfile("./pbapp/static/json/shemas/wikimedia.json")

    def search_wiki(self, query):
        try:
            search = wikipedia.search(query)
            resume = wikipedia.summary(search[0], sentences=3)
        except wikipedia.exceptions.DisambiguationError as e:
            resume = "Toutes mes excuses mon canari, mais les informations que j'avais sur ce lieu ont dû être formatées !"

        return resume
