#!/usr/bin/env python
# -*- coding: utf-8 -*-

from NaoCreator.setting import *
from NaoCreator.Tool.speech_move import speech_and_move


def test_speech_move():
    Setting.naoPosture.goToPosture("Stand", 1.0)
    speech_and_move("Je suis content de manger le dimanche matin du saucisson, du roblechon avec un peu de"
                    "lait cru et notamment une pincée de vermicelles. ")
