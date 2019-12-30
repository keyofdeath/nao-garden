#coding:utf-8
                      
                      
def script(s, player=None):
    from NaoQuest.objective import Objective
    from NaoCreator.setting import Setting
    if not player:
        Setting.error("Error in execution of post_script of objective \"objNomCapteur\": player is None")
        return
    if "bernard" in s.answer:
        player.current_scenario.cpt_name = "Bernard"
    elif any(w in s.answer for w in ("giselle", "gisèle")):
        player.current_scenario.cpt_name = "Giselle"
