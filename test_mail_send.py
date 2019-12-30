#!/usr/bin/env python
# -*- coding: utf-8 -*-
from NaoCreator.setting import Setting
Setting(nao_connected=False, debug=True, nao_quest_v="2.0", ip="192.168.0.1")
from NaoCreator.Tool.mailor import nao_send_mail

nao_send_mail("swanoublanc@yahoo.fr", "test", "coucou c'est nao le petit robot c'est un test")
