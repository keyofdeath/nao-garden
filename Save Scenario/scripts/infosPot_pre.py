#coding:utf-8
                      
                      
def script(s, player=None):
    from NaoQuest.objective import Objective
    from NaoCreator.setting import Setting
    from NaoSensor.jardin import Jardin
    if not player:
        Setting.error("Error in execution of pre_script of objective \"infosPot\": player is None")
        return

    if not hasattr(player.current_scenario, "jardin"):
        player.current_scenario.jardin = Jardin()
    
    s.question = s.question.format(player.current_scenario.cpt_name, len(player.current_scenario.jardin.pots) + 1)
