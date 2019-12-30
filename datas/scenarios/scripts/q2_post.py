#coding:utf-8
                      
                      
def script(s, player=None):
    from NaoQuest.objective import Objective
    from NaoCreator.Tool.speech_move import speech_and_move
    from NaoCreator.setting import Setting
    if not player:
        Setting.error("Error in execution of post_script of objective \"q2\": player is None")
        return

    if hasattr(s, "kw_answer"):

        if s.kw_answer == "python":
            player.point += 1
            speech_and_move(u"Bravo ! tu as dit la bonne réponse !")