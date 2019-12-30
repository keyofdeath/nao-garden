# coding: utf-8
try:
    import NaoCreator.Tool.speech_move as sm
    import NaoCreator.SpeechToText.nao_key_reco as nkr

    from NaoQuest.objective import *
    from NaoCreator.SpeechToText.nao_listen import nao_listen
    from Interceptor.interceptor import typemsg
except Exception as e:
    print e


class InfoObjective(Objective):
    """
    Objectif de type "info", récupère une information donnée par l'utilisateur.
    Echoue si aucune réponse est renvoyée (taille de la réponse = 0).
    """
    def __init__(self, scenario_name="", quest_name="", inner_name=""):
        super(InfoObjective, self).__init__(scenario_name, quest_name, inner_name)

    def _exec(self):
        if not hasattr(self, "question"):
            print("Error! No \"question\" in InfoObjective \"{}\"".format(self.inner_name))
            return
        sm.speech_and_move(self.question)

    def _interact(self):
        self.failed_interact = False
        self.raw_answer = nao_listen().lower()
        if typemsg(self.raw_answer):
            self.answer = ""
            self.failed_interact = True
        else:
            self.answer = self.raw_answer  # nkr.sentence_keywords(self.raw_answer, self.keywords)

    def _verif(self):
        if self.failed_interact:
            return False
        return len(self.answer) > 0
