#coding:utf-8


def script(s, player=None):
    from NaoQuest.quest import Quest
    from NaoSensor.plant import Plant
    if not player:
        print("Error in execution of post_script \"testobj1_post\": player is None")
        return

    # on choppe la plante liée à cette quete pour modifier ce que doit dire nao
    s.desc = s.desc.format(player.current_quest.plante_lie.get_data(Plant.PLANTATION)["engrais"])


