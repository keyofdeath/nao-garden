#coding:utf-8
                      
                      
def script(s, player=None):
    from NaoQuest.objective import Objective
    from NaoCreator.setting import Setting
    from NaoCreator.Tool.speech_move import speech_and_move
    import NaoSensor.captor_data as Cp
    if not player:
        Setting.error("Error in execution of post_script of objective \"valeurJardin\": player is None")
        return
    c1 = Cp.CaptorData().get_data_from_csv_file(Cp.datas[0])
    c2 = Cp.CaptorData().get_data_from_csv_file(Cp.datas[1])
    speech_and_move(u"Le taux d'humidité du capteur {} est de {} pour cent".format(c1.get_data(c1.NICKNAME,0), c1.get_data(c1.SOIL_MOISTURE, 0)))
    speech_and_move(u"Le taux d'humidité du capteur {} est de {} pour cent".format(c2.get_data(c2.NICKNAME,0), c2.get_data(c2.SOIL_MOISTURE, 0)))
    speech_and_move(u"Le taux d'ensoleillement du capteur {} est de {}".format(c1.get_data(c1.NICKNAME,0), c1.get_data(c1.LIGHT, 0)))
    speech_and_move(u"Le taux d'ensoleillement du capteur {} est de {}".format(c2.get_data(c2.NICKNAME,0), c2.get_data(c2.LIGHT, 0)))
    speech_and_move(u"Le taux d'engrais du capteur {} est de {} pour cent".format(c1.get_data(c1.NICKNAME,0), c1.get_data(c1.FERTILIZER, 0)))
    speech_and_move(u"Le taux d'engrais du capteur {} est de {} pour cent".format(c2.get_data(c2.NICKNAME,0), c2.get_data(c2.FERTILIZER, 0)))
    speech_and_move(u"Le capteur {} perçoit une température de {} degrés".format(c1.get_data(c1.NICKNAME,0), c1.get_data(c1.TEMPERATURE, 0)))
    speech_and_move(u"Le capteur {} perçoit une température de {} degrés".format(c2.get_data(c2.NICKNAME,0), c2.get_data(c2.TEMPERATURE, 0)))
