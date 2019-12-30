# coding:utf-8


def script(s, player=None):
    from NaoQuest.objective import Objective
    from NaoCreator.setting import Setting
    from NaoCreator.Tool.speech_move import speech_and_move
    import NaoCreator.SGBDDialogue.creer as C
    if not player:
        Setting.error("Error in execution of post_script of objective \"ValidationRemplirTerre\": player is None")
        return
    if not s.completed:

        # on recupaire le position de l'objectif courent dans la list
        index_curent_obj = player.current_quest.objectives.index(s)
        # on mais l'onjectif présédent comme non valider pour que nao reise les instruction
        player.current_quest.objectives[index_curent_obj - 1].completed = False
        p1 = C.Creer(C.Reponse, 41, 42, 43, 44)
        speech_and_move(u"{}".format(p1.out()))
    else:
        p1 = C.Creer(C.Reponse, 37, 38, 39, 40)
        speech_and_move(u"{}".format(p1.out()))