#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
GNU AFFERO GENERAL PUBLIC LICENSE
    Version 3, 19 November 2007
"""
import sys

reload(sys)
sys.setdefaultencoding('utf8')

from naoqi import ALProxy
from logging.handlers import RotatingFileHandler

import NaoSensor.captor_data as cd
import logging
import inspect


class Setting:
    def __init__(self, **kwargs):
        if hasattr(Setting, "initialized") and not kwargs.get("override", False):
            return
        print("Initializing NaoSettings...")
        #
        # _________________/INIT LOGGER\________________________
        Setting.logger = logging.getLogger()
        Setting.logger.setLevel(kwargs.get("logger_level", logging.ERROR))
        formatter = logging.Formatter('%(asctime)s :: %(levelname)s :: %(message)s')

        #
        file_handler = RotatingFileHandler('activity.log', 'a', 1000000, 1)
        file_handler.setLevel(kwargs.get("logger_level", logging.ERROR))
        file_handler.setFormatter(formatter)

        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(kwargs.get("logger_level", logging.ERROR))
        stream_handler.setFormatter(formatter)
        #

        Setting.logger.addHandler(file_handler)
        Setting.logger.addHandler(stream_handler)

        # settings NaoQuest
        Setting.NAO_QUEST_V = kwargs.get("nao_quest_v", "2.0")

        # Si Nao est connecté et disponible => True
        Setting.NAO_CONNECTED = kwargs.get("nao_connected", True)
        Setting.BYPASS_WAIT_FOR = kwargs.get("bypass_wait_for", not Setting.NAO_CONNECTED)
        Setting.USE_MIC = kwargs.get("use_mic", False)
        Setting.DEBUG = kwargs.get("debug", False)
        Setting.LOAD_CPT_DATA = kwargs.get("load_cpt_data", False)

        # Connexion
        Setting.ROBOT_IP = kwargs.get("ip", "192.168.0.1")
        Setting.PORT = kwargs.get("port", 9559)

        #                   _______________________
        # _________________/VAR POUR LE SERVER MAIL\________________________
        Setting.mail_adresse = "TODO"
        Setting.password = "TODO"

        #                   _______________________
        # _________________/CONSTANTES NAO SCENARIO\________________
        # Nom de la zone mémoire affectée pour récupérer la valeur des visages détectés
        Setting.MEMORY_FACE = "Face"
        # Intervale pour récuperer les données des visages
        Setting.FACE_DETECTION_RECOGNITION_PERIOD = 500
        # Nombre max de visage inconnus mais potentiellement mal detectés
        Setting.LIMIT_OF_UNKNOWN_FACE = 5
        # Nombre max de visage connus avent de décider qu'on le connait bien.
        Setting.LIMIT_OF_KNOWN_FACE = 2

        #                   ____________________
        # _________________/CONSTANTE NAO LISTEN\________________
        # Nombre max d'essais de reconnaissance vocale
        Setting.LIMIT_RECOGNITION_TRIES = 5
        # chanel qui choisit les micro d'enregistrement.
        Setting.CHANEL = [0,  # left
                          0,  # right
                          1,  # front
                          0]  # hear
        # Nombre de bruits minimums pour considérer que la personne a commencée à parler
        Setting.MIN_SOUND_SPEAKING = 70
        # Temps minimal de l'enregistrement
        Setting.MIN_TIME_SPEAKING = 70
        # Ratio de silence minimums pour considérer que la personne a arreté de parler
        Setting.SILENCE_MIN_RATE = 0.95

        #                   ______________________
        # _________________/CONSTANTE MOVE PATTERN\________________
        Setting.NB_MOVE = 7
        Setting.NB_CHARS_MOVE_THRESHOLD = 100

        #                   ______________
        # _________________/PROXY POUR NAO\________________________
        if Setting.NAO_CONNECTED:
            Setting.naoFaceDetectionRecognition = ALProxy("ALFaceDetection", Setting.ROBOT_IP, Setting.PORT)
            Setting.naoSpeech = ALProxy("ALTextToSpeech", Setting.ROBOT_IP, Setting.PORT)
            Setting.naoMemoryProxy = ALProxy("ALMemory", Setting.ROBOT_IP, Setting.PORT)
            Setting.naoLed = ALProxy("ALLeds", Setting.ROBOT_IP, Setting.PORT)
            Setting.naoMotion = ALProxy("ALMotion", Setting.ROBOT_IP, Setting.PORT)
            Setting.naoFaceTracker = ALProxy("ALFaceTracker", Setting.ROBOT_IP, Setting.PORT)
            Setting.naoAudioRecorder = ALProxy("ALAudioRecorder", Setting.ROBOT_IP, Setting.PORT)
            Setting.naoSoundDetection = ALProxy("ALSoundDetection", Setting.ROBOT_IP, Setting.PORT)
            Setting.naoLandMarkProxy = ALProxy("ALLandMarkDetection", Setting.ROBOT_IP, Setting.PORT)
            Setting.naoPosture = ALProxy("ALRobotPosture", Setting.ROBOT_IP, Setting.PORT)
        else:
            import NaoSimulator.say
            import NaoSimulator.naoMemory

            from mock import MagicMock

            Setting.naoFaceDetectionRecognition = MagicMock()
            Setting.naoSpeech = NaoSimulator.say
            Setting.naoMemoryProxy = NaoSimulator.naoMemory
            Setting.naoLed = MagicMock()
            Setting.naoMotion = MagicMock()
            Setting.naoFaceTracker = MagicMock()
            Setting.naoAudioRecorder = MagicMock()
            Setting.naoSoundDetection = MagicMock()
            Setting.naoLandMarkProxy = MagicMock()
            Setting.naoPosture = MagicMock()

        #                   _____________
        # _________________/INIT CAPTEURS\________________________
        if Setting.LOAD_CPT_DATA:
            cd.CaptorData(time_delta=200)
            Setting.cptdata = [cd.CaptorData.get_data_from_csv_file(nickname)
                               for nickname in cd.datas]
        else:
            Setting.cptdata = []

        Setting.initialized = True
        Setting.CURRENT_PLAYER = None

        print("...Done")

    @staticmethod
    def log(level, msg):
        func = inspect.currentframe().f_back.f_code
        Setting.logger.log(level, "{}.{}: {}".format(func.co_name, func.co_firstlineno, msg))

    @staticmethod
    def error(msg):
        Setting.log(logging.ERROR, msg)

    @staticmethod
    def info(msg):
        Setting.log(logging.INFO, msg)

    @staticmethod
    def critical(msg):
        Setting.log(logging.CRITICAL, msg)

    @staticmethod
    def debug(msg):
        Setting.log(logging.DEBUG, msg)

    @staticmethod
    def warning(msg):
        Setting.log(logging.WARNING, msg)


def log(errorlevel, msg):
    Setting.log(errorlevel, msg)
