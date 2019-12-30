#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
GNU AFFERO GENERAL PUBLIC LICENSE
    Version 3, 19 November 2007
"""
try:
    from globals_nao_quest import config
    from NaoCreator.SpeechToText import nao_key_reco
    from NaoCreator.SpeechToText.nao_listen import nao_listen
    from os.path import isfile
    from NaoCreator.setting import Setting

    import importlib
    import json
    import NaoCreator.Tool.speech_move as sm
    import copy
    import imp
except Exception as e:
    print e


class Objective(object):
    """
    Classe abstraite représentant un Objectif. Modifie elle-même sa classe selon le type de l'objectif qui lui est
    donné.
    """

    def __init__(self, scenario_name, quest_name, inner_name):
        """
        Construit un objectif à partir du nom du scénario, du nom de la quête et du nom de l'objectif.

        :param scenario_name: Le nom du scnéraio contenant l'objectif
        :param quest_name: Le nom de la quête contenant l'objectif
        :param inner_name: Le nom de l'objectif
        """

        if not scenario_name or not quest_name or not inner_name:
            return

        # On extrait le chemin relatif réel à partir de la config et des paramètres
        self.filepath = config["objectives"]["path"].format(scenario_name, quest_name, inner_name)

        self.inner_name = inner_name  # représente le nom du fichier sans l'extension
        self.scenario_name = scenario_name
        self.quest_name = quest_name

        # Attributs de base
        self.on_fail_exit = True
        self.completed = False
        self.failed_interact = False
        self.answer = ""
        self.xp = 0

        self.caller = None
        print self.filepath
        self.__dict__.update(json.load(open(self.filepath), "utf-8"))

        self.init_scripts()

        # on modifie la classe de l'objet créé afin d'utiliser les méthodes adéquates plutôt que
        # celles d'Objective
        if self.type:
            from NaoQuest.objectives.yn_question import YNQuestion
            from NaoQuest.objectives.info_objective import InfoObjective
            from NaoQuest.objectives.keyword_objective import KeyWordObjective
            from NaoQuest.objectives.custom_objective import CustomObjective
            from NaoQuest.objectives.cpt_objective import CptObjective
            if self.type == "yn":
                self.__class__ = YNQuestion
            elif self.type == "info":
                self.__class__ = InfoObjective
            elif self.type == "kw":
                self.__class__ = KeyWordObjective
            elif self.type == "custom":
                self.__class__ = CustomObjective
            elif self.type == "cpt":
                self.__class__ = CptObjective

    def init_scripts(self):
        print "Recréation des scripts..."
        # retro compa
        if Setting.NAO_QUEST_V == "2.0":
            pre = config["quest_scripts"]["path"].format(self.scenario_name, self.quest_name, self.inner_name, "pre")
            script = config["quest_scripts"]["path"].format(self.scenario_name, self.quest_name, self.inner_name, "script")
            post = config["quest_scripts"]["path"].format(self.scenario_name, self.quest_name, self.inner_name, "post")
        elif Setting.NAO_QUEST_V == "2.1":
            pre = config["scripts"]["path"].format(self.inner_name, "pre")
            script = config["scripts"]["path"].format(self.inner_name, "script")
            post = config["scripts"]["path"].format(self.inner_name, "post")
        else:
            Setting.critical("Bad Setting.NAO_QUEST_V version (= {})".format(Setting.NAO_QUEST_V))

        if isfile(pre):
            self.pre_script = imp.load_source("scripts", pre).script
        if isfile(script):
            self.script = imp.load_source("scripts", script).script
        if isfile(post):
            self.post_script = imp.load_source("scripts", post).script

    def __getstate__(self):
        """
        Permet de sérialiser l'objet sans les scripts (ils sont de toute manière ré-importés)
        :return: le state de l'objet en cours sans les scripts
        """
        d = copy.copy(self.__dict__)
        d.pop("pre_script", None)
        d.pop("script", None)
        d.pop("post_script", None)
        return d

    def _pres(self):
        """
        Présente l'objectif si l'attribut "pres" = True
        """

        if self.pres and hasattr(self, "name") and self.name:
            sm.speech_and_move(u"L'intitulé de cet objectif est. {}.".format(self.name))
        if hasattr(self, "desc") and self.desc:
            sm.speech_and_move(self.desc)

    def _exec(self):
        """
        Exécution interne de l'objectif, doit être redéfini par une sous-classe
        """
        raise Exception("Error! Using base \"Objective._exec\" instead of sub-class! ({})".format(self.inner_name))

    def _interact(self):
        """
        Interaction avec l'utilisateur (récupération de données)
        """
        raise Exception("Error! Using base \"Objective._interact\" instead of sub-class! ({})".format(self.inner_name))

    def _verif(self):
        """
        Fonction de vérification des données, doit retourner True ou False selon si les tests ont réussi.
        :return: True si la vérification a réussi, False sinon
        """
        raise Exception("Error! Using base \"Objective._verif\" instead of sub-class! ({})".format(self.inner_name))

    def _success(self):
        """
        Méthode exécutée lorsque _verif(1) réussi.
        """
        self.completed = True
        if hasattr(self, "text_on_success"):
            sm.speech_and_move(self.text_on_success)

    def _failed(self):
        """
        Méthode exécutée lorsque _verif(1) échoue.
        """
        self.completed = False
        if hasattr(self, "text_on_failed"):
            sm.speech_and_move(self.text_on_failed)

    def _pre_script(self, player=None):
        """
        Exécute le pre_script de l'objectif
        :param player: Le joueur en cours
        """
        self.pre_script(self, player)

    def _script(self, player=None):
        """
        Exécute le script de l'objectif
        :param player: Le joueur en cours
        """
        self.script(self, player)

    def _post_script(self, player=None):
        """
        Exécute le post_script de l'objectif
        :param player: Le joueur en cours
        """
        self.post_script(self, player)

    def _make_repeat(self):
        """
        Si l'attribut "repetable" est à True, alors, si l'objectif est completé, Nao demandera au joueur s'il veut
        recommencer cet objectif, le remettant alors à zéro.
        """
        if (getattr(self, "repeatable", False) or
                getattr(self, "repetable", False)) and self.completed:
            sm.speech_and_move("Cet objectif est répétable, veux-tu le recommencer ?")
            answer = nao_key_reco.sentence_keywords(nao_listen(), ["oui", "ouais", "affirmatif"])
            if answer:
                self.completed = False

    def __inner_execution(self, player=None):
        """
        Exécution interne de l'objectif, ne doit à prioris pas être redéfini dans une sous-classe.
        :param player: Le joueur en cours
        """
        self._exec()
        self._interact()

        if "script" in self.__dict__:
            self._script(player)

        self.success = self._verif()

        if self.success:
            self._success()
            if player:
                player.give_xp(self.xp)
        else:
            self._failed()

        if "post_script" in self.__dict__:
            self._post_script(player)

        self._make_repeat()

        return self.success

    def _finished(self):
        """
        Exécuté lorsque l'objectif termine
        """
        if hasattr(self, "text_on_finished"):
            sm.speech_and_move(self.text_on_finished)

    def launch(self, player=None):
        """
        Démarre l'objectif
        :param player: Le joueur en cours
        """

        self.init_scripts()

        if player:
            player.current_objective = self

        if "pre_script" in self.__dict__:
            self._pre_script(player)

        self._pres()
        # Boucle d'exécution interne
        while True:
            if self.__inner_execution(player=player):
                self._finished()
                return True
            elif not self.on_fail_exit:
                return False
