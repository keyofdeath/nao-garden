#!/usr/bin/env python
# -*- coding: utf-8 -*-

from NaoCreator.setting import Setting
Setting(nao_connected=False, debug=True, nao_quest_v="2.1", bypass_wait_for=True, ip="192.168.0.1")

from NaoQuest.questor import Questor
from PlayerManager.player_manager import Player

Player("swan").save()
q = Questor('InfoJardin', "swan")
q.launch()
q.player.save()