# coding:utf-8


def script(s, player=None):
    from NaoQuest.quest import Quest
    from NaoSensor.plant import Plant
    if not player:
        print("Error in execution of post_script \"testobj1_post\": player is None")
        return
    if hasattr(s, "kw_answer"):
        # Ajout de deux quetes pour preparer le terrain de la plante et planter la plante cool !!!
        print "post script c'est cool !!!"
        new_qst_preparer = Quest(player.current_scenario.inner_name, "preparerTerrain")
        new_qst_planter = Quest(player.current_scenario.inner_name, "planterGraine")

        # modification de la description
        new_qst_preparer.desc = new_qst_preparer.desc.format(s.kw_answer)
        new_qst_planter.desc = new_qst_planter.desc.format(s.kw_answer)
        new_qst_preparer.name = new_qst_preparer.name.format(s.kw_answer)

        p = Plant(s.kw_answer)

        # creation d'un attribut qui va contenir la plante liée à la quete
        new_qst_preparer.plante_lie = p
        new_qst_planter.plante_lie = p

        l = len(player.current_quest.next_quests)
        new_qst_preparer.branch_id = l + 1
        new_qst_planter.branch_id = l + 1

        if not p.get_data(Plant.PLANTATION).get("engrais", False):
            new_qst_preparer.pop_objective("engrais1")
            new_qst_preparer.pop_objective("engrais2")

        new_qst_preparer.next_quests.append(new_qst_planter)
        player.current_quest.next_quests.append(new_qst_preparer)

        print(u"Quete correctement ajoutée")
    else:
        print(u"Impossible d'ajouter la quete")

