class Message:
    def __init__(self):
        self.messages = {
            "home": {
                "01": "Bonjour monsieur",
                "02": "Salut le jeune",
                "03": "Quel bon vent t'ammène jeune pousse ?"
            },
            "message_geocode": "",
            "message_quest_after_geocode": {
                "01": "Mais t'ai-je déjà raconté l'histoire de ce quartier qui m'a vu en culottes courtes ?",
                "02": "Je dois trainer une casserole dans ce quartier, connais tu son histoire ? ",
                "03": "Pierre qui roule n'amasse pas mousse, connais tu l'histoire de ce lieu ? "
            },
            "message_wikimedia": ""
        }

    def message_home(self):
        """ Random rubrique homev"""
        pass

    def quest_user(self):
        """ First quest """
        pass

    def message_geocode(self):
        """ Retour API google map"""
        pass

    def message_quest_after_geocode(self):
        """ Quest GrandpyBot after geocode for story """
        pass

    def response_user_for_wiki(self):
        """ Bool, close quest user, go home """
        pass

    def message_wikimedia(self):
        """ Return API Wiki, close quest user, go home """
        pass
