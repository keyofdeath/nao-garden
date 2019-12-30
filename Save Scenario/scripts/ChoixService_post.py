#coding:utf-8
                      
                      
def script(s, player=None):
    from NaoQuest.quest import Quest
    from NaoCreator.setting import Setting
    import NaoCreator.Tool.speech_move as SM
    if not player:
        Setting.error("Error in execution of post_script of objective \"ChoixService\": player is None")
        return

    print s.__dict__
    if hasattr(s, "kw_answer"):
        print s.kw_answer
        # ajoue des quêtes en fonction du choix de l'utilisateur
        if s.kw_answer == "éxplication" or s.kw_answer == "éxplications":
            print "ajoue preparation jardin"
            new_qst = Quest(player.current_scenario.inner_name, "PreparationJardin")

        else:
            SM.speech_and_move(u"Ajoue de l'arrosage")
            print "ajoue arrosage"
            new_qst = Quest(player.current_scenario.inner_name, "Arrosage")

        l = len(player.current_quest.next_quests)
        new_qst.branch_id = l + 1

        player.current_quest.next_quests.append(new_qst)

