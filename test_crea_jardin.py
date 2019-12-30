# coding: utf-8
from NaoCreator.setting import Setting
Setting(nao_connected=False, debug=True, bypass_wait_for=True, nao_quest_v="2.1", ip="192.168.0.1")

from NaoQuest.questor import Questor

# Player("swan").save()
q = Questor('demo', "swan")
q.launch()
q.player.save()
