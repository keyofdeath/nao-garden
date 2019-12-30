# coding:utf-8


def script(s, player=None):
    from NaoQuest.objective import Objective
    from NaoCreator.setting import Setting
    from NaoCreator.Tool.speech_move import speech_and_move
    if not player:
        Setting.error("Error in execution of post_script of objective \"q1\": player is None")
        return

    if hasattr(s, "kw_answer"):

        if s.kw_answer == "2" or s.kw_answer == "deux":
            player.current_quest.point += 1
            speech_and_move(u"Félicitation tu a la bonne réponse.")
        else:
            speech_and_move(u"mauvaise réponse ! La bonne réponse était. 2.")

        speech_and_move(u"Voici l'explication : Une plante vivace ou plante pérenne est une plante vivant "
                        u"plus de deux ans. Ces plantes résistent au gel et à la sécheresse, "
                        u"elles se régénèrent toutes seules.")