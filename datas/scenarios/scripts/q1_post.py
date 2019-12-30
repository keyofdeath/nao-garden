#coding:utf-8
                      
                      
def script(s, player=None):
    from NaoQuest.objective import Objective
    from NaoCreator.setting import Setting
    from NaoCreator.Tool.speech_move import speech_and_move
    if not player:
        Setting.error("Error in execution of post_script of objective \"q1\": player is None")
        return

    if hasattr(s, "kw_answer"):
        player.point = 0
        if s.kw_answer == "linux":
            player.point += 1
            speech_and_move(u"Bravo ! tu as dit la bonne réponse !")