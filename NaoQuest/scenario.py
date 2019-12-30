#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
GNU AFFERO GENERAL PUBLIC LICENSE
    Version 3, 19 November 2007
"""
try:
    from globals_nao_quest import config
    from NaoCreator.setting import Setting
    import json
    import NaoCreator.Tool.speech_move as sm
    import NaoQuest.quest as q
    import NaoCreator.SpeechToText.nao_key_reco as nkr
    import NaoCreator.SpeechToText.nao_listen as nl
    import codecs
except Exception as e:
    print e


class Scenario(object):
    """
    Représente un Scénario gérant sa propre exécution.
    """
    def __init__(self, inner_name):
        """
        Charge un scénario selon son nom
        :param name: Le nom du scénario
        """
        self.inner_name = inner_name
        self.filepath = config["scenarios"]["path"].format(inner_name)

        # default values
        self.name = ""
        self.desc = ""
        self.pres = True
        self.next_scenario = list()
        self.completed = False
        self.xp = 0

        self.caller = None

        self.__dict__.update(json.load(open(self.filepath), "utf-8"))

        self.starting_quest = q.Quest(inner_name, self.starting_quest)
        self.next_scenario = [Scenario(name) for name in self.next_scenario]

    def _pres(self):
        """
        Présente le scénario si l'attribut "pres" = True
        """
        if hasattr(self, "pres") and not self.pres:
            return
        if hasattr(self, "name") and self.name:
            sm.speech_and_move(u"L'intitulé de cet objectif est. {}.".format(self.name))
        if hasattr(self, "desc") and self.desc:
            sm.speech_and_move(self.desc)

        self.pres = False

    def launch(self, player=None):
        """
        Démarre le Scénario
        :param player: Le joueur démarrant le Scénario
        :return: True si l'exécution termine le scénario (completed=True), False sinon
        """
        if player:
            player.current_scenario = self

        self._pres()

        if self.starting_quest is None:
            print("Error! Scenario {} has no starting quest!".format(self.inner_name))
            return True

        todo = self.starting_quest.choose_quest()
        if todo:
            if len(todo) == 1:
                todo[0].caller = self
                todo[0].launch(player)
            else:
                sm.speech_and_move(u"Il y a plusieurs quêtes disponibles. Laquelle veux-tu executer?")
                kws = ["première", "2e" if not Setting.NAO_CONNECTED else "deuxième",
                       "troisième", "quatrième", "cinquième", "sixième"]
                sm.speech_and_move(u"".join([u"La {} s'intitule {}.".format(kws[i], todo[i].name) for i in range(len(todo))]))
                msg = codecs.encode(nl.nao_listen().lower(), "utf-8")
                rep = nkr.sentence_keywords(msg, kws)
                if not rep:
                    print("Non reconnu !")
                    return False

                todo[kws.index(rep[0])].caller = self
                todo[kws.index(rep[0])].launch(player)

        todo = self.starting_quest.choose_quest()
        if not todo:
            self.completed = True

            # give xp
            if player:
                player.give_xp(self.xp)

            return True
        else:
            return False
