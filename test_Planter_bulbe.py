#!/usr/bin/env python
# -*- coding: utf-8 -*-
from NaoCreator.setting import Setting
Setting(nao_connected=False, debug=True, bypass_wait_for=False, nao_quest_v="2.1", load_cpt_data=False, ip="169.254.88.3", USE_MIC=False)

from NaoQuest.questor import Questor
from PlayerManager.player_manager import Player
from NaoSimulator.get_mic_input import record

Player("swan").save()
q = Questor('PlanterBulbe', "swan")
q.launch()
q.player.save()


