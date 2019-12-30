#coding:utf-8
                      
                      
def script(s, player=None):
    from NaoQuest.objective import Objective
    from NaoCreator.setting import Setting
    import NaoCreator.Tool.facebookor as FC
    if not player:
        Setting.error("Error in execution of pre_script of objective \"result\": player is None")
        return
    if 0 <= player.current_quest.point <= 3:
        s.question = s.question.format(str(player.current_quest.point) + u" point. "
                                                                         u"Tu peux faire mieux! "
                                                                         u"N'hésite pas a recommencer ce qcm")
    elif 4 <= player.current_quest.point <= 7:
        s.question = s.question.format(str(player.current_quest.point) + u" point. "
                                                                         u"Pas mal !")
    else:
        s.question = s.question.format(str(player.current_quest.point) + u" point. "
                                                                         u"G,G")
        FC.send_the_post("Le jardinier {} a marquer {} "
                         "point dans la quête du QCM! GG a lui !".format(player.player_name,
                                                                         player.current_quest.point))