#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
GNU AFFERO GENERAL PUBLIC LICENSE
    Version 3, 19 November 2007
"""
try:
    import cPickle
    import NaoCreator.Tool.facebookor as FC
    import NaoCreator.Tool.speech_move as SM
    from NaoCreator.setting import Setting
except Exception as e:
    print e


class Player(object):
    """
    Représente un utilisateur (joueur).
    """
    def __init__(self, player_name=""):
        """
        Créer un joueur à partir de son nom.
        :param player_name: Le nom du joueur
        """
        self.player_name = player_name
        self.xp = 0
        self.level = 1
        self.exp_needed = 5
        self.current_scenario = None
        self.current_quest = None
        self.current_objective = None
        self.scenarios = []

    def set_current_scenario(self, scenario):
        """
        Modifie le scénario actuel du joueur.
        :param scenario: Le nouveau scénario du joueur
        """
        self.current_scenario = scenario
        if scenario not in self.scenarios:
            self.scenarios += [scenario]

    def save(self):
        """
        Sauvegarde le joueur dans un fichier.
        """
        import os
        if not os.path.exists('datas/player_data/{}'.format(self.player_name)):
            os.mkdir('datas/player_data/{}'.format(self.player_name))
        cPickle.dump(self, open('datas/player_data/{}/{}.play'.format(self.player_name, self.player_name), 'wb'))
        print("Sauvegarde du joueur effectuée avec succès !")

    @staticmethod
    def load(player_name):
        """
        Charge et retourne une instance de joueur à partir de son nom.
        :param player_name: Le nom du joueur a charger.
        """
        player = cPickle.load(open('./datas/player_data/{}/{}.play'.format(player_name, player_name), 'rb'))
        return player

    def level_up(self):
        """
        Augmente le niveau du joueur de 1.
        :return:
        """
        self.level += 1
        self.exp_needed += 4 + self.level
        try:
            FC.send_the_post("Le jardinier {} vient d'évoluer au niveau {} ! ┏(:|])┛┗(:))┓┗(:D)┛┏(8|)┓".format(self.player_name, self.level))
        except Exception as e:
            print e
        SM.speech_and_move("Bravo tu a évolué au niveau {} ! Je vais le signaler sur ma page Facebook".format(self.level))
        Setting.info("Level up! Le joueur {} a atteint le niveau {}.".format(self.player_name, self.level))

    def give_xp(self, amount):
        self.xp += amount
        while self.xp >= self.exp_needed:
            self.level_up()

