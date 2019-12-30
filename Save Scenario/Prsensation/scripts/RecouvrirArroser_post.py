#coding:utf-8
                      
                      
def script(s, player=None):
    from NaoQuest.objective import Objective
    from NaoCreator.setting import Setting
    if not player:
        Setting.error("Error in execution of post_script of objective \"RecouvrirArroser\": player is None")
        return
    if not s.completed:
        s.wait_for = False