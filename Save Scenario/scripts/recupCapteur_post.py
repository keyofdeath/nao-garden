#coding:utf-8
                      
                      
def script(s, player=None):
    from NaoQuest.objective import Objective
    from NaoCreator.setting import Setting
    if not player:
        Setting.error("Error in execution of post_script of objective \"recupCapteur\": player is None")
        return

    player.current_quest.captor_in_use = s.answer[0]
