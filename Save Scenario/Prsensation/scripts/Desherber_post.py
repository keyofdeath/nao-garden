#coding:utf-8
                      
                      
def script(s, player=None):
    from NaoQuest.objective import Objective
    from NaoSensor.plant import Plant
    import NaoCreator.SGBDDialogue.creer as bd
    import NaoCreator.Tool.speech_move as sm
    if not player:
        print("Error in execution of post_script \"testobj1_post\": player is None")
        return

    if not s.completed:
        p1 = bd.Creer(bd.Instruction, bd.DicoVide, 30)
        p2 = bd.Creer(bd.Instruction, bd.DicoVide, 31)
        p3 = bd.Creer(bd.Instruction, bd.DicoVide, 32)
        p4 = bd.Creer(bd.Instruction, bd.DicoVide, 33)
        sm.speech_and_move(p1.out() + p2.out() + p3.out() + p4.out())
        s.completed = True
    else:
        s.wait_for = False
