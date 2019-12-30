#!/usr/bin/env python
# -*- coding: utf-8 -*-
from NaoCreator.setting import *
from NaoCreator.nao_scenario_creator import nao_scenario_module


def i_meet_you():
    Setting.naoSpeech.say("Je t'ai vu")
    return


def i_know_you():
    return


def start_stop_test():
    print "Demarage du start_stop_test"
    print "Toucher son pied gauche pour terminer le teste"

    nao_scenario_module(i_meet_you, i_know_you)


if __name__ == '__main__':
    start_stop_test()
