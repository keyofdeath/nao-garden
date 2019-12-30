#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
GNU AFFERO GENERAL PUBLIC LICENSE
    Version 3, 19 November 2007
"""
from NaoCreator.setting import Setting


def sitdown():
    """
    Assoit Nao
    :return:
    """
    Setting.naoPosture.goToPosture("Sit", 1.0)


def emergency_stop():
    """
    Fonction qui arrête le programme en cas d'interruption
    :return:
    """
    Setting.naoSpeech.say("Arret de nao scenario")
    Setting.naoLed.off("AllLeds")
    Setting.naoMotion.setStiffnesses("Head", 0.0)
    try:
        Setting.naoFaceDetectionRecognition.unsubscribe(Setting.MEMORY_FACE)
    except Exception as e:

        print e

    try:
        Setting.naoFaceDetectionRecognition.enableRecognition(False)
    except Exception as e:
        print e

    try:
        Setting.naoFaceTracker.stopTracker()
    except Exception as e:
        print e

    try:
        Setting.naoAudioRecorder.stopMicrophonesRecording()
    except Exception as e:
        print e

    try:
        Setting.naoSoundDetection.unsubscribe("SoundDetected")
    except Exception as e:
        print e

        # naoPosture.goToPosture("Sit", 1.0)


def normal_stop():
    """
    Fonction qui arrête le programme normalement, pour arrêter le suiveur de visage et la reconaissance de visage
    :return:
    """
    Setting.naoSpeech.say("Arret de nao scenario")
    Setting.naoLed.off("AllLeds")
    Setting.naoMotion.setStiffnesses("Head", 0.0)
    Setting.naoFaceDetectionRecognition.unsubscribe(Setting.MEMORY_FACE)
    Setting.naoFaceDetectionRecognition.enableRecognition(False)
    Setting.naoFaceTracker.stopTracker()
    # naoPosture.goToPosture("Sit", 1.0)
    quit()


if __name__ == '__main__':
    from NaoCreator.setting import Setting
    Setting(nao_connected=True)
    emergency_stop()
    # sitdown()
