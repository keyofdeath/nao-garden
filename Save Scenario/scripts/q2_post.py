# coding:utf-8


def script(s, player=None):
    from NaoQuest.objective import Objective
    from NaoCreator.setting import Setting
    from NaoCreator.Tool.speech_move import speech_and_move
    if not player:
        Setting.error("Error in execution of post_script of objective \"q1\": player is None")
        return

    if hasattr(s, "kw_answer"):

        if s.kw_answer == "1" or s.kw_answer == "un":
            player.current_quest.point += 1
            speech_and_move(u"Félicitation tu a la bonne réponse.")
        else:
            speech_and_move(u"mauvaise réponse ! La bonne réponse était. 1.")

        speech_and_move(u"Voici l'explication : Le printemps est la période la plus favorable pour rempoter ses plantes."
                        u"C'est une saison marquée par la reprise de la végétation."
                        u"A contrario, on proscrit le rempotage l'hiver, époque à laquelle les plantes sont au repos.")