#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
GNU AFFERO GENERAL PUBLIC LICENSE
    Version 3, 19 November 2007
Script a utiliser quand on allume Nao la première fois
"""
try:
    from NaoCreator.setting import *
    Setting(nao_connected=True, debug=True, ip="169.254.88.3")

    import NaoCreator.SpeechToText.nao_listen as Nl
    import NaoCreator.Tool.speech_move as Sm
    import NaoCreator.Tool.stop as Stp
except Exception as e:
    print e

if __name__ == '__main__':

    Sm.speech_and_move(u"Démarrage du script !")
    try:
        Sm.speech_and_move(u"{}".format(Nl.nao_listen()))
    except Exception as e:
        print "Error start: ", e
        Stp.emergency_stop()
