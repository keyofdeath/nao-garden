#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
GNU AFFERO GENERAL PUBLIC LICENSE
    Version 3, 19 November 2007
"""
try:
    from NaoQuest.wait_for import wait_for
    from PlayerManager.player_manager import Player
    from NaoCreator.setting import Setting
    from NaoQuest.scenario import Scenario

    import NaoCreator.Tool.stop as stp
    import NaoQuest.scenario as scn
    import NaoCreator.Tool.speech_move as sm
    import NaoCreator.SpeechToText.nao_listen as nl
    import NaoCreator.SpeechToText.nao_key_reco as nkr
    import os.path
except Exception as e:
    print e


class Questor:
    """
    Gère l'exécution des Scénarios
    """
    def __init__(self, scn_name, player_name, starting_scn=None, ending_scn=None):
        """
        
        :param scn_name: 
        :param player_name: 
        :param starting_scn: 
        :param ending_scn: 
        """
        if os.path.exists('./datas/player_data/{}/{}.play'.format(player_name, player_name)):
            self.player = Player().load(player_name)
        else:
            self.player = Player(player_name)

        Setting.CURRENT_PLAYER = self.player

        if self.player.current_scenario is None:
            self.scenario = scn.Scenario(scn_name)
            self.player.set_current_scenario(self.scenario)
        else:
            self.scenario = self.player.current_scenario

        self.starting_scn = starting_scn
        self.ending_scn = ending_scn

        self.stoped = False

    def launch(self):
        """
        Démarre l'exécution du questor, termine lorsque le joueur change ou lorsque l'exécution est terminée.
        """
        scn_end = False
        if self.starting_scn:
            Scenario(self.starting_scn).launch(self.player)

        self.player.set_current_scenario(self.scenario)
        while not self.stoped:
            self.player.current_scenario.caller = self
            if not self.player.current_scenario.launch(self.player):
                # Si le scénario courant, la quête courante ou l'objectif courant possède l'attribut "wait_for",
                # alors il est prioritaire.
                # Note: par défaut, l'attribut est à Faux sauf pour l'objective où il est à True.
                if max(getattr(self.player.current_scenario, "wait_for", False),
                       getattr(self.player.current_quest, "wait_for", False),
                       getattr(self.player.current_objective, "wait_for", True)):
                    if wait_for(self.player):
                        scn_end = False
                        self.stop()
            else:
                if not self.next_scn():
                    scn_end = True
                    self.stop()

        if self.ending_scn:
            Scenario(self.ending_scn).launch(self.player)

        return scn_end

    def next_scn(self):
        """
        Modifie le scénario actuel en trouvant le scénario suivant.
        :return: False si il n'y a pas de scénario suivant, True sinon.
        """
        todo = [s for s in self.player.current_scenario.next_scenario if not s.completed]
        if not todo:
            return False
        if len(todo) == 1:
            self.player.set_current_scenario(todo[0])
            return True

        sm.speech_and_move(u"Il y a plusieurs scénarios disponibles. Lequel veux-tu executer?")
        kws = ["premier", "2e" if not Setting.NAO_CONNECTED else "deuxième",
               "troisième", "quatrième", "cinquième", "sixième"]
        sm.speech_and_move(u"".join([u"Le {} s'intitule {}.".format(kws[i], todo[i].name) for i in range(len(todo))]))
        msg = nl.nao_listen().lower()
        rep = nkr.sentence_keywords(msg, kws)
        if not rep:
            print("Non reconnu !")
            return False
        self.player.set_current_scenario(Scenario(self.player.current_scenario.next_scenario[kws.index(rep)]))
        return True

    def stop(self):
        """
        Stoppe le Questor et Nao
        """
        print("Stopping Questor...")
        self.player.save()
        self.stoped = True
        print("Stoped.")
