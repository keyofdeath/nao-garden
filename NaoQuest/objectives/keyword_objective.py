# coding: utf-8
"""
GNU AFFERO GENERAL PUBLIC LICENSE
    Version 3, 19 November 2007
Script a utiliser quand on allume Nao la première fois
"""
try:
    from NaoQuest.objective import *
    from NaoCreator.SpeechToText.nao_listen import nao_listen
    from NaoCreator.setting import Setting
    from Interceptor.interceptor import typemsg

    import NaoCreator.Tool.speech_move as sm
    import NaoCreator.SpeechToText.nao_key_reco as nkr
except Exception as e:
    print e


class KeyWordObjective(Objective):
    """
    Objectif de type "kw", réussit si l'utilisateur dit un mot-clef contenu dans la liste "keywords".
    Permet d'ajouter un attribut "kw2id", permettant de gérer les alias/les pluriels.
    """

    def __init__(self, scenario_name="", quest_name="", inner_name=""):
        super(KeyWordObjective, self).__init__(scenario_name, quest_name, inner_name)

    def _exec(self):
        if not hasattr(self, "question"):
            Setting.error("No \"question\" in KeyWordObjective \"{}\"".format(self.inner_name))
            return
        if not hasattr(self, "keywords"):
            Setting.error("No \"keywords\" in KeyWordObjective \"{}\"".format(self.inner_name))
            return
        sm.speech_and_move(self.question)

    def _interact(self):
        self.failed_interact = False
        self.raw_answer = nao_listen().lower()

        if typemsg(self.raw_answer):
            self.answer = list()
            self.failed_interact = True
            return

        # On fait dire à Nao les différents mots-clefs
        if nkr.sentence_keywords(self.raw_answer, ["aide", "ed"]):
            if hasattr(self, "help_kw"):
                sm.speech_and_move(self.help_kw)
            else:
                sm.speech_and_move("Les mots clefs disponibles sont. {}".format(
                    ". ".join([self.kw2id[i] for i in self.kw2id])
                ))
            self.completed = False
            self.answer = list()

        # On extrait la réponse selon keywords puis kw2id
        self.answer = nkr.sentence_keywords(self.raw_answer, self.keywords)
        if len(self.answer) == 1:
            if self.answer[0] in self.kw2id:
                self.kw_answer = self.kw2id[self.answer[0]]
            else:
                self.kw_answer = self.answer[0]
        # On échoue si on repère plus d'un mot-clef
        elif len(self.answer) > 1:
            sm.speech_and_move("Vous avez dit plus d'un mot-clef !")
            self.answer = []
            self.completed = False

    def _verif(self):
        if self.failed_interact:
            return False
        return len(self.answer) > 0
