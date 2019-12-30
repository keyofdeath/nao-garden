#coding:utf-8
                      
                      
def script(s, player=None):
    from NaoQuest.objective import Objective
    from NaoCreator.setting import Setting
    if not player:
        Setting.error("Error in execution of pre_script of objective \"planterCapteur\": player is None")
        return

    s.question = s.question.format(["premier", "deuxième", "troisième", "quatrième", "cinquième", "sixième", "septième", "huitième", "neuvième", "dixième"][s.caller.branch_id - 1])
