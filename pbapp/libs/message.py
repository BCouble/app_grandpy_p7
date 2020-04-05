import random


class Message:
    def __init__(self):
        self.messages = {
                "home": {
                    0: "Bonjour monsieur, une question ?",
                    1: "Salut le jeune !",
                    2: "Quel bon vent t'ammène jeune pousse ?"
                },
                "geocode": {
                    0: "Bien sûr mon poussin ! Voici l'adresse : ",
                    1: "J'ai trouvé le jeune : ",
                    2: "C'est ici que l'on pousse le mieux : "
                },
                "wiki_story": {
                    0: "Mais t'ai-je déjà raconté l'histoire de ce quartier qui m'a vu en culottes courtes ?",
                    1: "Je dois trainer une casserole dans ce quartier, connais tu son histoire ? ",
                    2: "Pierre qui roule n'amasse pas mousse, connais tu l'histoire de ce lieu ? "
                },
                "error_mes": {
                    0: "Grandpy comprend rien le jeune ! Aurais-tu oublié un tirêt ? Reformule ta question !",
                }
            }
        self.message_ge_wi = []

    def random(self):
        rand = random.randint(0, 2)

        return rand

    def message_home(self):
        """ Random rubrique home"""
        message = self.messages["home"][self.random()]

        return message

    def message_geocode(self):
        """ Retour API google map"""
        message = self.messages["geocode"][self.random()]
        self.message_ge_wi.append(message)

    def message_wikimedia(self):
        """ Bool, close quest user, go home """
        message = self.messages["wiki_story"][self.random()]
        self.message_ge_wi.append(message)

        return self.message_ge_wi

    def message_error(self):
        """ Return quest grandpy fail """

        return self.messages["error_mes"][0]
