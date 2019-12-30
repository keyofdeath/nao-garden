#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
GNU AFFERO GENERAL PUBLIC LICENSE
    Version 3, 19 November 2007
"""

from NaoCreator.setting import *
from random import randint

import NaoCreator.MovePattern.move as Mp
import NaoCreator.MovePattern.stand_up as Sp
import codecs


def speech_and_move(text_to_say):
    """
    Fonction qui fait bouger nao pendant qu'il parle
    INFO: Si le message est court Nao ne bougera pas (voir fichier setting.py pour changer la longueur)
    ATTENTION: Nao doit être debout !!!!!!!
    :param text_to_say: texte à dire
    :return:
    """

    if len(text_to_say) <= Setting.NB_CHARS_MOVE_THRESHOLD:
        Setting.naoSpeech.say(codecs.encode(text_to_say, "utf-8"))
        return

    pid = Setting.naoSpeech.post.say(codecs.encode(text_to_say, "utf-8"))
    move_cc = randint(1, Setting.NB_MOVE)
    while Setting.naoSpeech.wait(pid, 1):
        names, times, keys = Mp.dico_move['move'+str(move_cc)]
        Setting.naoMotion.angleInterpolation(names, keys, times, True)
        move_cc += 1
        if move_cc > Setting.NB_MOVE:
            move_cc = 1
    try:
        Setting.naoMotion.angleInterpolation(Sp.names, Sp.keys, Sp.times, True)
    except Exception as e:
        print "Error ", e
        Setting.naoPosture.goToPosture("Stand", 0.6)
    # onregarde vers le haut
    # naoMotion.angleInterpolation(Mlup.names, Mlup.keys, Mlup.times, True)
