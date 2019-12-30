# coding:utf-8


def script(s, player=None):
    from NaoQuest.objective import Objective
    from NaoSensor.plant import Plant
    import NaoCreator.SGBDDialogue.creer as bd
    import NaoCreator.Tool.speech_move as sm
    if not player:
        print("Error in execution of post_script \"testobj1_post\": player is None")
        return

    if not s.completed:
        p1 = bd.Creer(bd.Instruction, bd.DicoVide, 34, 35, 36)
        sm.speech_and_move(p1.out())
        sm.speech_and_move(u"Pour cette plante, tu dois : {}".format(player.current_quest.plante_lie.get_data(Plant.PLANTATION)["arroser"]))

