#coding:utf-8
                      
                      
def script(s, player=None):
    from NaoQuest.objective import Objective
    from NaoCreator.setting import Setting
    from NaoSensor.captor_data import cpt_giselle, CaptorData
    if not player:
        Setting.error("Error in execution of pre_script of objective \"InfoJardin\": player is None")
        return

    s.desc = s.desc.format(cpt_giselle.data[0][CaptorData.SOIL_MOISTURE], cpt_giselle.data[0][CaptorData.TEMPERATURE])
