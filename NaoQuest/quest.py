#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
GNU AFFERO GENERAL PUBLIC LICENSE
    Version 3, 19 November 2007
"""
try:
    from globals_nao_quest import config
    import json
    import NaoCreator.Tool.speech_move as sm
    import NaoQuest.objective as o
except Exception as e:
    print e


class Quest:
    """
    Représente une quête gérant sa propre exécution.
    """
    def __init__(self, scenario_name="", inner_name=""):
        """
        Charge une quête selon son nom et son scénario
        """
        if not scenario_name or not inner_name:
            return

        # On extrait le chemin relatif réel à partir de la config et des paramètres
        self.filepath = config["quests"]["path"].format(scenario_name, inner_name)

        self.inner_name = inner_name  # représente le nom du fichier sans l'extension
        # default values
        self.scenario_name = scenario_name
        self.pres = True
        self.branch_id = 0  # id de la branche sur laquelle est située la quête
        self.next_quests = list()
        self.objectives = list()
        self.prerequisite = list()
        self.completed = False
        self.started = False

        self.caller = None

        self.__dict__.update(json.load(open(self.filepath), "utf-8"))

        # On instancie les quêtes et objectifs
        self.objectives = [o.Objective(scenario_name, inner_name, obj_name) for obj_name in self.objectives]
        self.next_quests = [Quest(scenario_name, quest_name) for quest_name in self.next_quests]

    def init_scripts(self):
        for s in self.objectives:
            s.init_scripts()

    def pop_objective(self, inner_name):
        """
        Retire un objectif de la liste des objectifs de cette quête.
        :param inner_name: Le nom interne de l'objectif à retirer
        """
        for o in self.objectives:
            if o.inner_name == inner_name:
                self.objectives.remove(o)
                break

    def _pres(self):
        """
        Présente la quête si l'attribut "pres" = True
        """
        if hasattr(self, "pres") and not self.pres:
            return

        if "name" in self.__dict__:
            sm.speech_and_move(u"L'intitulé de cette quête est. {}.".format(self.name))
        if "desc" in self.__dict__:
            sm.speech_and_move(self.desc)

        self.pres = False

    def launch(self, player=None):
        """
        Démarre la quête
        :param player: Le joueur en cours
        """

        self.started = True

        if player:
            player.current_quest = self

        self._pres()

        # On récupère les objectifs non terminés
        todo = [o for o in self.objectives if not o.completed]
        if todo:
            todo[0].caller = self
            todo[0].launch(player=player)

        todo = [o for o in self.objectives if not o.completed]
        if not todo:
            self.completed = True

            # give xp
            if player:
                player.give_xp(self.xp)

            return True
        else:
            return False

    def choose_quest(self):
        """
        Détermine quelle est la/les prochaine(s) quête(s) à exécuter
        :return: La/les prochaine(s) quête(s) à exécuter
        """
        if not self.completed:
            return [self]

        res = []
        final = []
        for q in self.next_quests:

            # si elle n'a pas été commencée c'est une quete que l'on peut faire
            if not q.started:
                res += [q]

            else:
                if self.branch_id == q.branch_id:
                    res += q.choose_quest()
                else:
                    # branchement, on regarde si une branche a été commencée, si oui on la termine d'abord
                    l = q.choose_quest_with_same_branch(q.branch_id)
                    if l:
                        return l
                    else:
                        # si toute la branche a été completée, on ajoute la quete de fin de branchement
                        final = q.choose_quest()
        if res:
            return res
        # si toutes les branches ont étées terminées, on renvoie la quete finale (ou [] s'il n'y a pas de branchement)
        else:
            return final

    def choose_quest_with_same_branch(self, branch_id):
        """
        Retourne les quêtes non completées sur la même branche.
        :param branch_id: L'id de la branche a regarder
        :return: Les quêtes non completées sur la branche "branch_id"
        """
        if self.branch_id != branch_id:
            return []

        if not self.completed:
            return [self]

        res = []
        for q in self.next_quests:
            res += q.choose_quest_with_same_branch(branch_id)
        return res
