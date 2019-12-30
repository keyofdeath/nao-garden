# coding: utf-8
"""
GNU AFFERO GENERAL PUBLIC LICENSE
    Version 3, 19 November 2007
Script a utiliser quand on allume Nao la première fois
"""
try:

    from NaoQuest.objective import *
    from NaoCreator.setting import Setting
    from NaoCreator.SpeechToText.nao_listen import nao_listen
    from NaoCreator.Tool.stop import normal_stop

except Exception as e:
    print e


class CptObjective(Objective):
    """
    Objectif de type "Capteur", pour réussir, le capteur que l'on interroge doit contenir des valeurs dans des plages
    de données spécifiées par deux dictionnaires de valeurs: "cpt_min", "cpt_max".
    Champs obligatoires:
        - cpt_min:  Dictionnaire représentant les valeurs minimales que le capteur doit renvoyer pour réussir
        - cpt_max:  Dictionnaire représentant les valeurs maximales que le capteur doit renvoyer pour réussir
        - nickname: Le nom du capteur que l'on regarde
    Champs optionnels:
        - since:    A partir de quel quart d'heure depuis le dernier on extrait les données
        - to:       Jusqu'à quel quart d'heure depuis le dernier on extrait les données
        - avg:      Détermine si les valeurs regardées sont la moyenne des valeurs regardées

        Note: since <= to
    """
    def __init__(self, scenario_name="", quest_name="", inner_name=""):
        super(CptObjective, self).__init__(scenario_name, quest_name, inner_name)

    def _exec(self):
        if not hasattr(self, "values_min") or not hasattr(self, "values_max"):
            Setting.error("No \"values_min / values_max\" in CptObjective \"{}\"".format(self.inner_name))
            return
        if not hasattr(self, "nickname"):
            Setting.critical("No \"nickname\" in CptObjective \"{}\"".format(self.inner_name))
            return

    def _interact(self):
        pass

    def _verif(self):
        cpt = None
        for c in Setting.cptdata:
            print c, c.get_data("nickname"), self.nickname
            if c.get_data("nickname") == self.nickname:
                cpt = c
                break
        if cpt is None:
            Setting.critical("Could not initialize CaptorData in \"CptObjective {}\"".format(self.inner_name))
            normal_stop()

        for i in range(getattr(self, "since", 0), getattr(self, "to", 0)+1):
            for k in self.values_min:
                if c.get_data(k, i) < self.values_min[k]:
                    return False
            for k in self.values_max:
                if c.get_data(k, i) > self.values_max[k]:
                    return False

        return True
