# coding: utf-8
from NaoCreator.setting import Setting
Setting(nao_connected=True, debug=True, nao_quest_v="2.1", bypass_wait_for=False, load_cpt_data=False, ip="169.254.88.3")

from NaoQuest.questor import Questor
from NaoQuest.scenario import Scenario
from PlayerManager.player_manager import Player
from NaoQuest.objectives.cpt_objective import CptObjective

Player("tristan").save()
q = Questor('demo', "tristan")
q.launch()
