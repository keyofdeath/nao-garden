#coding:utf-8
                      
                      
def script(s, player=None):
    from NaoQuest.objective import Objective
    from NaoQuest.quest import Quest
    from NaoCreator.setting import Setting
    import NaoCreator.Tool.speech_move as sm

    if not player:
        Setting.error("Error in execution of post_script of objective \"nbPots\": player is None")
        return

    if not s.completed:
    	return

    try:
    	player.nb_pots = int(s.answer)

    	for i in range(player.nb_pots):
    		q = Quest(s.scenario_name, "infosPotN")
    		q.name = q.name.format(["premier", "deuxième", "troisième", "quatrième", "cinquième", "sixième", "septième", "huitième", "neuvième", "dixième"][i])

    		q.branch_id = i + 1
    		s.caller.next_quests += [q]
    except Exception as e:
    	sm.speech_and_move("Je n'ai pas réussi à comprendre un nombre !")
    	s.completed = False
