#coding:utf-8


def script(s, player=None):
    from NaoQuest.objective import Objective
    from NaoCreator.setting import Setting
    from NaoSensor.plant import Plant
    from NaoCreator.Tool.speech_move import speech_and_move
    if not player:
        Setting.error("Error in execution of post_script of objective \"ChoixBulbe\": player is None")
        return
    if hasattr(s, "kw_answer"):

        if s.kw_answer == "1":
            p = Plant("glaieul")
            speech_and_move(u"Très bon choix le glaieul est l'une de mes fleur préférer.")
        elif s.kw_answer == "2":
            p = Plant("lys")
            speech_and_move(u"Tu a bien fait de choisir un lys.")
        else:
            print "3"
            p = Plant("freesias")
            speech_and_move(u"Sa tombe bien, c'est justement la saison des freesias")

        # creation d'un attribut qui va contenir la plante liée au joueur
        player.plante_lie = p

        print(u"Quete correctement ajoutée")