# coding: utf-8
from NaoCreator.setting import Setting
Setting(nao_connected=False, debug=True, nao_quest_v="2.1", ip="192.168.0.1")

from NaoQuest.questor import Questor
from PlayerManager.player_manager import Player

Player("boby").save()
q = Questor('Absence', "boby")
q.launch()
q.player.save()
