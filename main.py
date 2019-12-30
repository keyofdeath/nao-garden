#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
GNU AFFERO GENERAL PUBLIC LICENSE
    Version 3, 19 November 2007
"""
try:
    from NaoCreator.setting import Setting
    # Setting(nao_connected=True, debug=True, nao_quest_v="2.1", ip="192.168.0.1")
    Setting(nao_connected=True, debug=True, nao_quest_v="2.1", ip="169.254.88.3")
    from NaoCreator.nao_scenario_creator import i_meet_you, nao_scenario_module
    import NaoCreator.SGBDDialogue.creer as Dg
    import NaoCreator.Tool.speech_move as Sm
    import NaoCreator.SpeechToText.nao_key_reco as Nkr
    from PlayerManager.player_manager import Player
    from NaoQuest.questor import Questor
    from NaoQuest.scenario import Scenario
    import speech_recognition as sr
except Exception as e:
    print e


def waitfor():
    """
    Attend que l'utilisateur appuie sur le haut de la tête de nao
    :return:na
    """
    print u"Attente d'une réponse pour la prochaine quête"
    Setting.naoLed.off("AllLeds")
    Setting.naoLed.on("AllLedsRed")
    while Setting.naoMemoryProxy.getData("MiddleTactilTouched") != 1:
        pass
    Setting.naoLed.off("AllLeds")
    Setting.naoLed.on("AllLedsGreen")


def start_quest_mode(player_name):
    """
    Fonction qui commence les quêtes de l'utilisateur
    :param player_name: nom du joueur
    :return:
    """
    print "start load"
    # On reprend la progression du joueur, s'il est nouveau on fait le scénario d'intro
    # quest = Questor("IntroNaoGarden", player_name)

    scn_end = False
    while not scn_end:
        quest = Questor("PlanterBulbe", Setting.CURRENT_PLAYER.player_name if Setting.CURRENT_PLAYER else player_name)
        print "start lauch"
        scn_end = quest.launch()
        quest.player.save()


def active_traker():
    """
    active le suivi des visages
    :return:
    """
    Setting.naoFaceTracker.startTracker()


def desactive_traker():
    """
    désactive le suivi des visages
    :return:
    """
    Setting.naoFaceTracker.stopTracker()


def admin(face_name):
    """
    Petite fonction secrète pour donner des ordres à Nao
    :param face_name: nom du visage devant nao
    :return:
    """
    Sm.speech_and_move(u"Mots de passe".format(face_name))
    password = Nkr.nao_key_word_recognition("cancer")
    # bon mots de passe
    if password != "":
        Sm.speech_and_move(u"Bienvenu maitre {}! Attention il me faut de la place pour mes mouvements."
                           u"Pour arrêter dit moi fini ou fin. Quand je fini une action appuie sur ma tête"
                           u"Dis moi ce que tu veux "
                           .format(face_name))

        posture_key_word = {"assis":"Sit", "debout":"Stand",
                          "coucher":"LyingBack", "couché":"LyingBack", "ventre":"LyingBelly",
                          "pause":"SitRelax", "méditer":"Crouch", "méditation":"Crouch"}
        end_key_word = ["fin", "fini", "arret", "stop"]
        desactive_traker()
        while True:
            try:

                res = Nkr.nao_key_word_recognition(*posture_key_word.keys() + end_key_word)
                if res in posture_key_word:
                    Setting.naoPosture.goToPosture(posture_key_word[res], 1.0)
                elif res in end_key_word:
                    Sm.speech_and_move(u"Fin de la session admin !")
                    break
                waitfor()
                # que veux-tu de moi
                text1 = Dg.Creer(Dg.Demande, Dg.DicoVide, 7, 8)
                Sm.speech_and_move(u"{}".format(text1.out()))
            except Exception as e:
                print("Erreur: ", e)
        active_traker()
    else:
        Sm.speech_and_move(u"Mots de passe incorrect. Auto destruction amorcée")


def menu(player_name):
    """
    Menu principal
    :param player_name: nom du joueur courant
    :return:
    """

    admin_key_word = ["admin", "administrateur", "administration"]
    quest_start_key_word = ["apprentissage", "quête", "formation", "mission"]
    end_key_word = ["fin", "fini", "arret", "stop"]

    # que veux-tu de moi
    text1 = Dg.Creer(Dg.Demande, Dg.DicoVide, 7, 8)
    Sm.speech_and_move(u"{}.".format(text1.out()))

    # Menu
    while True:

        res = Nkr.nao_key_word_recognition(*admin_key_word + quest_start_key_word + end_key_word)
        # Commande secrete
        if res in admin_key_word:
            admin(player_name)
            Setting.naoPosture.goToPosture("Stand", 1.0)

        # Il veut faire ses quêtes
        elif res in quest_start_key_word:
            # On démarre les quêtes super
            start_quest_mode(player_name)

        # si on veut quitter
        elif res in end_key_word:
            break

        # Si la personne se trompe
        else:
            Sm.speech_and_move(u"Dommage je n'ai pas compris ce que tu a dis, peux-tu répéter ?")
        waitfor()
        # que ve tu de moi
        text1 = Dg.Creer(Dg.Demande, Dg.DicoVide, 7, 8)
        Sm.speech_and_move(u"{}.".format(text1.out()))

    Sm.speech_and_move(u"Dommage tu vas me manquer! C'est pas grave à plus. Bisous")


def i_know_you_local(face_name):
    """
    Fonction appelée par nao creator quand nao connait la personne
    :param face_name: nom de la personne
    :return:
    """
    # bonjour prenom
    text1 = Dg.Creer(Dg.MotsUtiles, {"prenom": face_name}, 8, 37)
    Sm.speech_and_move(u"{}".format(text1.out()))
    # on regarde si le joueur n'existe pas déja dans les fichier
    # menu(face_name)
    start_quest_mode(face_name)


def i_meet_you_local():
    """
    Fonction qui enregistre la personne que nao ne connait pas
    :return:
    """

    name = i_meet_you()
    if name != "":
        i_know_you_local(name)


def main():
    """

    :return:
    """
    Player("Roger").save()
    Player("Thomas").save()
    nao_scenario_module(i_meet_you_local, i_know_you_local)


if __name__ == "__main__":
    # naoPosture.goToPosture("Stand", 1.0)
    # start_quest_mode("swan")
    main()
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(u"| Attente d'une réponse |")
        audio = r.listen(source)

    try:
        msg = r.recognize_google(audio, language="fr-FR").lower()
        print "=> %s" % msg
    except sr.UnknownValueError:
        print("[get_mic_input.record] Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("[get_mic_input.record] Could not request results from Google Speech Recognition service; {0}".format(e))
    """
