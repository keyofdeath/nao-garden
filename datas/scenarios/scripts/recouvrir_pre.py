#coding:utf-8
                      
                      
def script(s, player=None):
    from NaoQuest.objective import Objective
    from NaoCreator.setting import Setting
    from NaoSensor.plant import Plant
    if not player:
        Setting.error("Error in execution of pre_script of objective \"recouvrir\": player is None")
        return

    s.desc = s.desc.format(player.plante_lie.get_data(Plant.PLANTATION)["recouvrir"])