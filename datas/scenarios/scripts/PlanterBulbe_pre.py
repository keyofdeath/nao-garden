#coding:utf-8
                      
                      
def script(s, player=None):
    from NaoQuest.objective import Objective
    from NaoCreator.setting import Setting
    from NaoSensor.plant import Plant
    if not player:
        Setting.error("Error in execution of pre_script of objective \"PlanterBulbe\": player is None")
        return
    print "ici = ", player.plante_lie
    print "ici = ", player.plante_lie.get_data(Plant.NOM)
    s.desc = s.desc.format(player.plante_lie.get_data(Plant.PLANTATION)["creuser"] + " Puis, " + player.plante_lie.get_data(Plant.PLANTATION)["planter"])