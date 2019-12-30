#coding:utf-8
                      
                      
def script(s, player=None):
    from NaoQuest.quest import Quest
    from NaoCreator.setting import Setting
    import NaoCreator.Tool.speech_move as sm
    import NaoCreator.Tool.mailor as MA
    import codecs

    if not player:
        Setting.error("Error in execution of post_script of objective \"ChoixArrosage\": player is None")
        return

    if s.completed:
        # on chop le mail template
        f = codecs.open("datas/mailTemplate/mailArrosage", 'r', encoding='utf-8')
        text = '\n'.join(f.readlines())
        mail = MA.get_user_mail()
        # on l'envoie est on récupaire le mail de l'utilisateur
        MA.nao_send_mail(mail, "Aide arrosage automatique", text)
        sm.speech_and_move(u"Je tes envoyer un mail avec tout se qui faut savoir sur l'arrosage automatique.")
    else:
        s.completed = True