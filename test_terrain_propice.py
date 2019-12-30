# coding: utf-8
from NaoCreator.setting import Setting
Setting(nao_connected=False, debug=True, nao_quest_v="2.1", bypass_wait_for=True, load_cpt_data=False, use_mic=False, ip="192.168.0.1")

from NaoQuest.questor import Questor
from NaoQuest.scenario import Scenario
from PlayerManager.player_manager import Player

from NaoQuest.objectives.cpt_objective import CptObjective

Player("tristan").save()
q = Questor('terrainPropice', "tristan")
q.launch()
