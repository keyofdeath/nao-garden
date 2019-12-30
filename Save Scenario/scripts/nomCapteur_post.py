#coding:utf-8
                      
                      
def script(s, player=None):
    from NaoQuest.objective import Objective
    from NaoCreator.setting import Setting
    from NaoSensor.jardin import Jardin
    if not player:
        Setting.error("Error in execution of post_script of objective \"nomCapteur\": player is None")
        return

    if s.kw_answer == u"gisèle":
        s.kw_answer = "Giselle"
    elif s.kw_answer == "bernard":
        s.kw_answer = "Bernard"
    else:
        print "???"

    player.current_scenario.captorName = s.kw_answer
    player.current_scenario.jardin = Jardin()
