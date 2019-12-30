#coding:utf-8
                      
                      
def script(s, player=None):
    from NaoQuest.objective import Objective
    from NaoCreator.setting import Setting
    from NaoSensor.captor_data import cpts
    from NaoSensor.jardin import Pot
    import NaoCreator.Tool.speech_move as sm

    if not player:
        Setting.error("Error in execution of post_script of objective \"recupInfoPot\": player is None")
        return

    jardin = player.current_scenario.jardin
    print cpts, player.current_scenario.captorName
    cpt = cpts[player.current_scenario.captorName]
    pot = Pot(cpt.get_datas())
    if jardin.reg_pot(pot):
        sm.speech_move("Le pot a été ajouté avec succès !")
    else:
        sm.speech_move("Impossible d'ajouter le pot, n'aurais-tu pas ajouté le même pot ou pas attendu assez ?")
