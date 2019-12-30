#coding:utf-8
                      
                      
def script(s, player=None):
    from NaoQuest.objective import Objective
    from NaoCreator.setting import Setting
    from NaoSensor.plant import Plant
    if not player:
        Setting.error("Error in execution of pre_script of objective \"FinEtRecolte\": player is None")
        return
    # on choppe la plante liée à cette quete pour modifier ce que doit dire nao
    s.desc = s.desc.format(player.current_quest.plante_lie.get_data(Plant.RECOLTE))
