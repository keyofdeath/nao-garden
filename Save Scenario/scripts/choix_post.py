#coding:utf-8


def script(s, player=None):
    from NaoQuest.objective import Objective
    from NaoCreator.setting import Setting
    from NaoQuest.quest import Quest
    if not player:
        Setting.error("Error in execution of post_script of objective \"choix\": player is None")
        return

    if hasattr(s, "kw_answer"):

        if s.kw_answer == "qcm" or s.kw_answer == "QCM":
            new_qst = Quest(player.current_scenario.inner_name, "qcm")
            new_qst.point = 0
        else:
            new_qst = Quest(player.current_scenario.inner_name, "info")

        l = len(player.current_quest.next_quests)
        new_qst.branch_id = l + 1
        player.current_quest.next_quests.append(new_qst)

