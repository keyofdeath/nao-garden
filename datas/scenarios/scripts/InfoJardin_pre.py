#coding:utf-8
                      
                      
def script(s, player=None):
    from NaoQuest.objective import Objective
    from NaoCreator.setting import Setting
    from NaoSensor.captor_data import cpt_giselle, CaptorData
    from NaoCreator.Tool.speech_move import speech_and_move
    from time import sleep
    if not player:
        Setting.error("Error in execution of pre_script of objective \"InfoJardin\": player is None")
        return
    try:

        tempetur = cpt_giselle.data[0][CaptorData.TEMPERATURE]
    except Exception as e:

        print e
        tempetur = 20

    if -50 <= tempetur <= -1:
        text = u"IL fait trop froit ! Tu vie au pole Nord ?"
    elif 0 <= tempetur <= 5:
        text = u"C'est trop froit pour t-on bullbe. Je te conseil de le rentrée au chaut"
    elif 6 <= tempetur <= 11:
        text = u"Il fait un peut froit pour t-on bullbe."
    elif 12 <= tempetur <= 19:
        text = u"La températur est un peut just. Je te conseille de rentrée t-on bulbe le matin. " \
               u"Est des qu'il fait plus chaud, tu peut le sortire"
    elif 20 <= tempetur <= 29:
        text = u"La température est très bien."
    elif 30 <= tempetur <= 32:
        text = u"Il commence a fire chaud ! Il faut bien pensser a aroser t-on bulbe. Mais que quand le soleil est coucher pour éviter de bruller t-on bulbe."
    elif 33 <= tempetur <= 35:
        text = u"Il fait trop chaud ! Rentre t-on pôt a l'intèrieur pour protéger t-on bulbe de la charleur"
    else:
        text = u"je ne peut rien dire"
    speech_and_move(u"Maintenemps que tu a mit le capteur dans t-on peau. Je vais regarder le température.")
    sleep(1)
    s.desc = s.desc.format(text)