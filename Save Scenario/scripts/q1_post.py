#coding:utf-8
                      
                      
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

        speech_and_move(u"Voici l'explication : Les billes d'argiles placées au fond du pot "
                        u"permettent d'assurer un bon drainage. "
                        u"C'est une étape primordiale à réaliser avant toute mise en pot au risque "
                        u"de voir les racines pourir par excès d'eau.")