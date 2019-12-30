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

        speech_and_move(u"Voici l'explication : Le paillage est une méthode pour protéger des excès de chaleur, "
                        u"de froid, limiter l'évaporation et empécher les mauvaises herbes. "
                        u"Il s'agit de recouvrir le sol avec une couche de paillis au début de la saison"
                        u"de culture et de renouveler l'opération si nécessaire.")