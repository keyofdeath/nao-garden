#!/usr/bin/env python
# -*- coding: utf-8 -*-
from NaoCreator.setting import Setting
Setting(nao_connected=True, debug=True, bypass_wait_for=True, nao_quest_v="2.1", ip="169.254.88.3")
from NaoCreator.Tool.stop import emergency_stop

if __name__ == '__main__':
    emergency_stop()