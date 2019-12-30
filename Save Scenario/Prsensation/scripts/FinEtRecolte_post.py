#coding:utf-8
                      
                      
def script(s, player=None):
    from NaoQuest.objective import Objective
    from NaoCreator.setting import Setting
    if not player:
        Setting.error("Error in execution of post_script of objective \"FinEtRecolte\": player is None")
        return
    if not s.completed:

        # on vire la phrase bravo tu a fini
        s.desc = '.'.join(s.desc.split(".")[2:])
