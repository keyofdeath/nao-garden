#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
GNU AFFERO GENERAL PUBLIC LICENSE
    Version 3, 19 November 2007
"""
import speech_recognition as sr
from NaoCreator.setting import Setting
import ftplib


def audio_to_text():
    """
    Fonction qui va récupérer le fichier audio téléchargé sur nao
    puis va l'envoyer au seveur Google speech to text
    :return: Le message en chaine de charactère ou renvoie une chaine vide
    s'il n'a pas réussi a reconnaître ce qui a été dit
    """
    # use "mono.wav" as the audio source
    r = sr.Recognizer()
    with sr.WavFile("msg.wav") as source:
        # read the entire WAV file
        audio = r.record(source)

    # recognize speech using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        msg = r.recognize_google(audio, language="fr-FR")
        if Setting.DEBUG:
            print("Google Speech Recognition found: " + msg)
        # on passe de unicode a str utf8
        msg = msg.encode('utf8')

        if Setting.DEBUG:
            # on dit le msg
            print "tu a dit {}.".format(msg)
        return msg

    except sr.UnknownValueError:
        if Setting.DEBUG:
            print("Google Speech Recognition could not understand audio")
        return ""

    except sr.RequestError as e:
        if Setting.DEBUG:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return ""


def download_msg(nao_record):
    """
    Fonction qui recupère l'enregistrement du serveur de nao puis le met en local sur le pc
    :return:
    """
    try:
        # on cree une fichier wav sur le pc
        local_wav = open("msg.wav", "wb")
        # on le telecharge depuis le serveyr ftp
        nao_record.retrbinary('RETR msg.wav', local_wav.write)
        # on fer la conection ftp
        local_wav.close()

    except Exception, e:
        print "error", e


def get_sound(tab_no_sound):
    """
    Fonction qui va compter le nombre de silence qu'il y a eu.
    S'il y a eu asser de silence et un minimum de bruit alors on arrête l'enregistrement
    :param tab_no_sound: Tableau de bruit ou silence 1=bruit 0=silence
    :return: Renvoie tab_no_sound : contient des 0 pour les silences et des 1 pour les bruits
    """
    tab = Setting.naoMemoryProxy.getData("SoundDetected")

    # si on a du silence et un minimum de son enregistré

    if tab[0][1] == 0 and tab_no_sound.count(1) > Setting.MIN_SOUND_SPEAKING:
        if Setting.DEBUG:
            print "Silence !"
        tab_no_sound.append(0)
        return tab_no_sound

    # si on a du bruit
    elif tab[0][1] == 1:
        if Setting.DEBUG:
            print "Bruit !"
        tab_no_sound.append(1)
        return tab_no_sound

    # on a du silence mais la personne n'a pas encore commencé à parler
    else:
        return tab_no_sound


def is_silence(tab_no_sound):
    """
    Fonction qui indique si la personne a fini de parler
    :param tab_no_sound: le tableau des 1 et 0
    :return: True si la personne a fini de parler, False sinon
    """
    l = len(tab_no_sound)
    if l < Setting.MIN_TIME_SPEAKING:
        return False
    else:
        ratio = tab_no_sound[l - Setting.MIN_TIME_SPEAKING:l].count(0)/float(Setting.MIN_TIME_SPEAKING)
        if ratio >= Setting.SILENCE_MIN_RATE and Setting.DEBUG:
            print "ratio : {}".format(ratio)
        return ratio >= Setting.SILENCE_MIN_RATE


def record_message(nao_record):
    """
    Cette fonction va enregistrer la voix de l'utilisateur pour pouvoir ensuite la passer au speech to text
    :return: le message en chaine de caractères
    """

    tab_no_sound = []
    end_recording_message = False

    # On commence l'enregistrement
    Setting.naoAudioRecorder.startMicrophonesRecording("/home/nao/msg.wav", "wav", 16000, Setting.CHANEL)

    Setting.naoLed.off("AllLeds")
    Setting.naoLed.on("AllLedsBlue")  # on allume toutes les led en bleu

    # Enregistrement du message
    while Setting.naoMemoryProxy.getData("MiddleTactilTouched") != 1 and not end_recording_message:

        tab_no_sound = get_sound(tab_no_sound)
        end_recording_message = is_silence(tab_no_sound)

    Setting.naoLed.off("AllLeds")
    Setting.naoLed.on("AllLedsGreen")
    Setting.naoAudioRecorder.stopMicrophonesRecording()
    download_msg(nao_record)
    return audio_to_text()


def recording(nao_record):
    """
    Cette fonction va lancer l'enregistrement pour l'utilisateur
    est va contrôler si le serveur google speech to text ne renvoie pas d'erreur
    :return: le message trouvé sinon une chaine vide
    """

    nb_try = 0
    msg = ""

    while msg == "" and nb_try < Setting.LIMIT_RECOGNITION_TRIES and \
                    Setting.naoMemoryProxy.getData("LeftBumperPressed") != 1:

        msg = record_message(nao_record)

        if Setting.DEBUG:
            print msg
        if msg == "":
            Setting.naoSpeech.say("Je n'ai pas compris ce que tu a dit. Peux-tu répéter ?")

        nb_try += 1

    if nb_try == Setting.LIMIT_RECOGNITION_TRIES and msg == "":
        Setting.naoSpeech.say("Je n'ai rien compris")

    return msg

try:

    if Setting.NAO_CONNECTED:
        def nao_listen():
            """
            Enregistre ce que dit l'utilisateur et en renvoie une chaîne de caractères
            :return: Une chaine de caractères de ce qu'a dit l'utilisateur
            """

            # Creer la classe pour se connecter au FTP
            nao_record = ftplib.FTP(Setting.ROBOT_IP)
            nao_record.login("nao", "nao")

            Setting.naoSoundDetection.subscribe("SoundDetected")
            msg = recording(nao_record).decode("utf-8")
            Setting.naoSoundDetection.unsubscribe("SoundDetected")
            return msg
    else:
        import NaoSimulator.get_mic_input as gmi
        nao_listen = gmi.record
except Exception as e:

    print e

"""
GNU AFFERO GENERAL PUBLIC LICENSE
    Version 3, 19 November 2007
"""