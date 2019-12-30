#coding:utf-8
                      
                      
def script(s, player=None):
    from NaoQuest.objective import Objective
    from NaoCreator.setting import Setting
    import NaoCreator.Tool.speech_move as sm
    if not player:
        Setting.error("Error in execution of post_script of objective \"obj2\": player is None")
        return

    if s.completed:
    	sm.speech_and_move("La phrase que tu as dite est: {}".format(s.raw_answer))
