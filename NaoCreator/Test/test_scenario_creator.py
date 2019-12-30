#!/usr/bin/env python
# -*- coding: utf-8 -*-
from NaoCreator.setting import *
from NaoCreator.nao_scenario_creator import nao_scenario_module, i_meet_you
from time import sleep


def i_meet_you_local():
    i_meet_you()
    return


def i_know_you_local(name_face):
    Setting.naoSpeech.say("Salut {}".format(name_face))
    sleep(1)
    return


def test_senario_creator():
    print "Demarage du test scenario creator"
    print "Toucher son pied gauche pour terminer le teste"

    nao_scenario_module(i_meet_you_local, i_know_you_local)


if __name__ == '__main__':
    test_senario_creator()

