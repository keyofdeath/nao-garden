#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
GNU AFFERO GENERAL PUBLIC LICENSE
    Version 3, 19 November 2007
"""
try:
    from NaoCreator.nao_scenario_creator import search_face, i_meet_you
    from NaoCreator.setting import Setting
    from time import sleep
    from PlayerManager.player_manager import Player

    import NaoCreator.Tool.speech_move as sm
except Exception as e:
    print e


def i_know_you(face_name, current_player):
    """
    Modifie le joueur actuel par celui qui a été reconnu par Nao.
    :param face_name: Le nom du joueur reconnu
    :param current_player: Le joueur actuel
    """
    if face_name == current_player.player_name:
        return
    current_player.save()
    Setting.CURRENT_PLAYER = Player(face_name)


def wait_for(current_player):
    """
    Attend un joueur. Celui-ci devra se montrer à Nao ou appuyer sur un bumper pour continuer l'exécution.
    :param current_player: Le joueur actuel
    """
    print "[wait_for] Waiting for player..."
    if Setting.BYPASS_WAIT_FOR:
        return False

    # On fait dire à Nao le text lors du wait_for
    if hasattr(current_player.current_objective, "wait_for_text"):
        sm.speech_and_move(current_player.current_objective.wait_for_text)
    elif hasattr(current_player.current_quest, "wait_for_text"):
        sm.speech_and_move(current_player.current_quest.wait_for_text)
    elif hasattr(current_player.current_scenario, "wait_for_text"):
        sm.speech_and_move(current_player.current_scenario.wait_for_text)

    nb_unknown_face = 0
    nb_known_face = 0
    pass_to_i_now_you = False

    Setting.naoLed.off("AllLeds")
    Setting.naoLed.on("AllLedsBlue")
    Setting.naoLed.on("AllLedsRed")

    i = 1

    old_player = current_player.player_name
    while Setting.naoMemoryProxy.getData("MiddleTactilTouched") != 1 and not pass_to_i_now_you:
        stop = Setting.naoMemoryProxy.getData("RightBumperPressed") == 1
        if stop:
            return False
        nb_unknown_face, nb_known_face, current_color, finished, pass_to_i_now_you = search_face(i_meet_you, i_know_you,
                                                                              nb_unknown_face, nb_known_face, "none",
                                                                              [current_player])
        sleep(.5)
        print i
        i += 1

    print old_player , Setting.CURRENT_PLAYER.player_name
    return old_player != Setting.CURRENT_PLAYER.player_name
