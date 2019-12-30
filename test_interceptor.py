# -*- coding: utf-8 -*-

from NaoCreator.setting import Setting
Setting(nao_connected=False, debug=True, ip="192.168.0.1")

from Interceptor.interceptor import typemsg

msg = raw_input("=> ")
typemsg(msg)
