#coding:utf-8
                      
                      
def script(s, player=None):
    from NaoQuest.objective import Objective
    from NaoCreator.setting import Setting
    from NaoSensor.plant import Plant
    if not player:
        Setting.error("Error in execution of pre_script of objective \"RemplirDeTerre\": player is None")
        return