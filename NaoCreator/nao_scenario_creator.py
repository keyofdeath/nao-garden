#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
GNU AFFERO GENERAL PUBLIC LICENSE
    Version 3, 19 November 2007
"""
from time import sleep
from NaoCreator.Tool.stop import normal_stop
from NaoCreator.setting import Setting

import NaoCreator.SGBDDialogue.creer as Dg
import NaoCreator.SpeechToText.nao_key_reco as Nkr
import NaoCreator.SpeechToText.nao_listen as Nl
import NaoCreator.Tool.face_reco as Fr
import NaoCreator.Tool.speech_move as Sm


def get_name():
    """
    Fonction qui obtient le nom de la personne.
    :return: Elle renvoie un couple (booleen, string)
    True et le nom si tout s'est bien passé
    False et un code d'erreur sinon
    """

    keyout = "non"
    name = ""

    while keyout != "" and Setting.naoMemoryProxy.getData("MiddleTactilTouched") != 1:
        try:
            name = Nl.nao_listen().decode("utf-8")
            # gestion des cas spéciaux
            if name == "":
                if Setting.DEBUG:
                    print"erreur sur NaoListen"
                return False, "erreur"

            elif "annuler" in name:
                if Setting.DEBUG:
                    print"annulation"
                return False, "annulation"

            elif "tu me connais" in name:
                if Setting.DEBUG:
                    print "re learning"
                return False, "re learning"

            Sm.speech_and_move(u"Le prénoms que tu ma dit est {} ".format(name))

            demande = Dg.Creer(Dg.Demande, Dg.DicoVide, 23)
            Sm.speech_and_move(u'{}'.format(demande.out()))
            # Si on a mal enregistré on le fait répéter
            keyout = Nkr.nao_key_word_recognition("non", "tu l'a mal dit")
            if keyout != "":
                Sm.speech_and_move(u"Désoler, peut tu me redire t-on prénom ?")
        except Exception as e:
            print e
            raise e
    return True, name


def waitfor():
    """
    Attend que l'utilisateur appuie sur le haut de la tête de nao
    :return:
    """
    print u"Attente d'une réponse pour la prochaine quête"
    Setting.naoLed.off("AllLeds")
    Setting.naoLed.on("AllLedsRed")
    while Setting.naoMemoryProxy.getData("MiddleTactilTouched") != 1:
        pass
    Setting.naoLed.off("AllLeds")
    Setting.naoLed.on("AllLedsGreen")


def i_meet_you():
    """
    Fonction qui est appelée si le visage détecté n'est pas reconnu.
    Cette fonction va enregistrer le nom de la personne puis son visage
    :return: Renvoie le nom du visage enregistré si tout se passe bien, renvoie une chaine vide si il y a une erreure
    """

    # Veux-tu enregistrer ton visage ?
    response = Dg.Creer(Dg.Demande, Dg.DicoVide, 51)
    Sm.speech_and_move(u"{}".format(response.out()))

    negative_answers = Nkr.nao_key_word_recognition("non", "pas", "nan", "annulation")

    # On a trouvé un mot clé négatif
    if negative_answers != "":
        Sm.speech_and_move(u"Annulation de l'enregistrement")
        return ""

    mots_utiles = Dg.Creer(Dg.MotsUtiles, Dg.DicoVide, 6, 7)
    demande = Dg.Creer(Dg.Demande, Dg.DicoVide, 20, 21, 22)
    Sm.speech_and_move(u'{} {}'.format(mots_utiles.out(), demande.out()))

    success, name = get_name()
    if not success:
        # On re enregistre le visage de la personne
        if name == "re learning":
            Sm.speech_and_move(u"Désoler ! j'ai du male enregistré t-on visage! peut tu me re dire t-on prénoms ?")
            while not success:
                success, name = get_name()

            Sm.speech_and_move(u"Parfait ! maintenemps je vais re apprendre t-on visage! Attention !")
            sleep(1)
            Fr.relearn_face(name)
            Sm.speech_and_move(u"Voila j'ai re apris t-on visage.")
        # Annulation de l'enregistrement
            return name
        else:
            return ""

    # content de te connaitre je vais enregistrer ton visage et instruction a faire
    if True:
        confimation = Dg.Creer(Dg.Confirmation, Dg.DicoVide, 49, 50)
        Sm.speech_and_move(u'{} {}'.format(confimation.out(), name))
    waitfor()
    Fr.add_face(name)
    confimation = Dg.Creer(Dg.Confirmation, Dg.DicoVide, 75, 76)
    # Je t'ai bien enregistré !
    Sm.speech_and_move(u'{}'.format(confimation.out()))

    return name


def search_face(func_i_meet_you, func_i_know_you, nb_unknown_face, nb_known_face, current_color, params=[]):
    """
    Regarde s'il y a un visage devant nao
    :param func_i_meet_you: fonction qui est appelée quand nao ne connait pas la personne
    :param func_i_know_you: fonction qui est appelée quand nao connait la personne
    :param nb_unknown_face: Nombre de visages inconnus détectés avant de valider le fait qu'il s'agit bien d'une nouvelle personne
    :param nb_known_face: Nombre de visages connus détectés avant de valider le fait qu'on le connait bien.
    :param current_color: Couleur des led courente
    :return: nouveau nombre de visage inconnus
    """
    data_face = Setting.naoMemoryProxy.getData("FaceDetected", 0)
    finished = False
    pass_to_i_now_you = False

    if Setting.DEBUG:
        print "visage : {}".format(data_face)

    # Si on voie un visage
    if data_face and len(data_face) == 5:

        if current_color == "green":
            Setting.naoLed.off("AllLeds")
            Setting.naoLed.on("AllLedsRed")
            current_color = "red"

        try:
            face_name = data_face[1][0][1][2]

            print "visage trouvé: {}".format(face_name)

            if face_name != "":
                # Visage connu
                if nb_known_face >= Setting.LIMIT_OF_KNOWN_FACE:
                    nb_unknown_face = 0
                    nb_known_face = 0
                    # Sm.speech_and_move(u"Bonjours {}".format(face_name))
                    Setting.naoLed.off("AllLeds")
                    Setting.naoLed.on("AllLedsGreen")
                    current_color = "green"
                    func_i_know_you(*([face_name] + params))
                    finished = True
                    pass_to_i_now_you = True

                # visage connu mais potentiellement mal détecté
                else:
                    nb_known_face += 1

            # Visage inconnu mais potentiellement mal detecté
            elif nb_unknown_face < Setting.LIMIT_OF_UNKNOWN_FACE:
                nb_unknown_face += 1

            # Visage incunnu
            else:
                nb_unknown_face = 0
                nb_known_face = 0
                Setting.naoLed.off("AllLeds")
                Setting.naoLed.on("AllLedsGreen")
                current_color = "green"
                func_i_meet_you()
                pass_to_i_now_you = False
                finished = True
        except Exception as e:

            if Setting.DEBUG:
                print "Error function search_face: {}".format(e)

    elif current_color == "red":
        Setting.naoLed.off("AllLeds")
        Setting.naoLed.on("AllLedsGreen")
        current_color = "green"

    return nb_unknown_face, nb_known_face, current_color, finished, pass_to_i_now_you


def nao_scenario_module(func_i_meet_you, func_i_know_you):
    """Fonction principale.
    :param func_i_meet_you: fonction qui est appelée quand nao ne connait pas la personne.
    :param func_i_know_you: fonction qui est appelée quand nao connait la personne.
    :return:
    """

    # Si nao est assie il
    Setting.naoPosture.goToPosture("Stand", 1.0)

    Setting.naoFaceDetectionRecognition.enableRecognition(True)

    # on autorise le proxy FaceDetectionRecognition a écrire dans la mémoire "Face"
    Setting.naoFaceDetectionRecognition.subscribe(Setting.MEMORY_FACE, Setting.FACE_DETECTION_RECOGNITION_PERIOD, 0.0)
    Setting.naoLed.on("AllLedsGreen")
    Setting.naoMotion.setStiffnesses("Head", 1.0)
    Setting.naoFaceTracker.startTracker()

    nb_unknown_face = 0
    nb_known_face = 0

    current_color = "green"

    Sm.speech_and_move(u"Démarage de nao création ! Initialisation des capteurs ! Tout le système et charger!")

    # Boucle principale
    while Setting.naoMemoryProxy.getData("LeftBumperPressed") != 1:
        nb_unknown_face, nb_known_face, current_color, finished, name = search_face(func_i_meet_you, func_i_know_you,
                                                                              nb_unknown_face, nb_known_face,
                                                                              current_color)
        sleep(0.5)

    normal_stop()
