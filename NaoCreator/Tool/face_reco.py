#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
GNU AFFERO GENERAL PUBLIC LICENSE
    Version 3, 19 November 2007
"""

from NaoCreator.setting import *


def add_face(face_name):
    """
    Fonction qui remet à jour le visage de la personne
    :param face_name: nom de la personne à ré-enregistrer
    :return:
    """
    # on allume toutes les led en bleu
    Setting.naoLed.off("AllLeds")
    Setting.naoLed.on("AllLedsBlue")

    face_name = face_name.encode("utf-8")
    result = Setting.naoFaceDetectionRecognition.learnFace(face_name)
    if result:
        Setting.naoSpeech.say("Je t'ai bien reconnu {}".format(face_name))
        print("OK !!!")
    else:
        Setting.naoSpeech.say("Je n'ai pas réussi")
        print "Error"


def relearn_face(face_name):
    """
    Fonction qui ré-apprend le visage qui est devant lui
    :param face_name: le nom de la personne à réapprendre
    :return: True si l'opération a réussie, False sinon
    """
    try:
        Setting.naoLed.on("AllLedsBlue")  # on allume toutes les led en bleu
        print "Re apprentissage du visage!"
        result = Setting.naoFaceDetectionRecognition.forgetPerson(face_name)
        if not result:
            Setting.naoSpeech.say("Ton prénom ne me dit rien ! Peut être qu'il a mal été dit ?")
            return False

        add_face(face_name)
        if result:
            Setting.naoSpeech.say("J'ai bien réussi a réapprendre ton visage {}".format(face_name))
            return True
        else:
            Setting.naoSpeech.say("Je n'ai pas réussi a réapprendre ton visage !")
            return False
    except Exception as e:
        print "error = ", e
