#coding:utf-8
                      
                      
def script(s, player=None):
    from NaoQuest.objective import Objective
    from NaoCreator.setting import Setting
    if not player:
        Setting.error("Error in execution of pre_script of objective \"resultat\": player is None")
        return
    s.desc = s.desc.format(player.point)