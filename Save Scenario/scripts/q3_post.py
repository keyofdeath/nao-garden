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

        speech_and_move(u"Voici l'explication : Le purin d'ortie est un insecticide naturel, peu couteux et efficace"
                        u"pour lutter contre les pucerons. C'est aussi un excellent engrais pour les plantes."
                        u"Pour le préparer, il suffit de laisser macérer 1 kg d'orties dans 10 litres d'eau "
                        u"pendant 2 à 3 jours.")