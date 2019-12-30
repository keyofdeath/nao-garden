#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
GNU AFFERO GENERAL PUBLIC LICENSE
    Version 3, 19 November 2007
"""
from NaoCreator.setting import Setting
import speech_recognition as sr


def record():
    """
    Récupère un fichier audio à partir du microphone de l'utilisateur.
    :return:
    """
    if not Setting.USE_MIC:
        return raw_input("=> ")

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(u"| Attente d'une réponse |")
        audio = r.listen(source)

    try:
        msg = r.recognize_google(audio, language="fr-FR").lower()
        print "=> %s" % msg
        return msg
    except sr.UnknownValueError:
        print("[get_mic_input.record] Google Speech Recognition could not understand audio")
        return ""
    except sr.RequestError as e:
        print("[get_mic_input.record] Could not request results from Google Speech Recognition service; {0}".format(e))
        return ""


