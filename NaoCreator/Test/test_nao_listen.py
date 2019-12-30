#!/usr/bin/env python
# -*- coding: utf-8 -*-

import NaoCreator.SpeechToText.nao_listen as Nl
from NaoCreator.setting import *


def test_naolisten():
    Setting.naoSpeech.say("Test d'une reponse courte !")
    Setting.naoSpeech.say("Test de se que tu ma dit {}".format(Nl.nao_listen()))

if __name__ == '__main__':
    test_naolisten()
