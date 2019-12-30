# coding: utf-8
"""
GNU AFFERO GENERAL PUBLIC LICENSE
    Version 3, 19 November 2007
Script a utiliser quand on allume Nao la première fois
"""
try:
    from NaoQuest.objective import *
    from NaoCreator.SpeechToText.nao_listen import nao_listen
    from Interceptor.interceptor import typemsg

    import NaoCreator.Tool.speech_move as sm
    import NaoCreator.SpeechToText.nao_key_reco as nkr
except Exception as e:
    print e


class YNQuestion(Objective):
    """
    Objective de type "yn", l'utilisateur doit simplement répondre part "oui" ou "non" (et ses alternatives) afin de
    réussir ou échouer l'objectif, cela dépendant de l'attribut "answer_yes".
    Si celui-ci est à True, l'utilisateur devra répondre "oui" pour réussir l'objectif, "non" sinon.
    """
    def __init__(self, scenario_name="", quest_name="", inner_name=""):
        super(YNQuestion, self).__init__(scenario_name, quest_name, inner_name)

    def _exec(self):
        if not hasattr(self, "question"):
            print("Error! No \"question\" in YNQuestion \"{}\"".format(self.inner_name))
            return
        sm.speech_and_move(self.question)

    def _interact(self):
        self.failed_interact = False
        self.raw_answer = nao_listen().lower()
        if typemsg(self.raw_answer):
            self.failed_interact = True
        else:
            self.answer = nkr.sentence_keywords(self.raw_answer, ["oui", "ouais", "affirmatif",
                                                                  "non", "nom", u"négatif"])

    def _verif(self):
        if self.failed_interact:
            return False
        if self.answer_yes:
            # Todo: Config mots-clefs "affirmatifs"
            return not set(self.answer).isdisjoint(["oui", "ouais", "affirmatif"])
        else:
            # Todo: Config mots-clefs "négatifs"
            return not set(self.answer).isdisjoint(["non", "nom", u"négatif"])
