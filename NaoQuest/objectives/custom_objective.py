# coding: utf-8
"""
GNU AFFERO GENERAL PUBLIC LICENSE
    Version 3, 19 November 2007
Script a utiliser quand on allume Nao la première fois
"""
try:

    from NaoQuest.objective import *
    import NaoCreator.Tool.speech_move as sm
    import NaoCreator.SpeechToText.nao_key_reco as nkr
    from NaoCreator.SpeechToText.nao_listen import nao_listen

except Exception as e:
    print e


class CustomObjective(Objective):
    """
    Objectif de type "custom", ne sait rien faire tout seul, toute l'exécution doit être faite à partir des
    post_script, script et pre_script.
    """
    def __init__(self, scenario_name="", quest_name="", inner_name=""):
        super(CustomObjective, self).__init__(scenario_name, quest_name, inner_name)

    def _exec(self):
        pass

    def _interact(self):
        pass

    def _verif(self):
        return True
