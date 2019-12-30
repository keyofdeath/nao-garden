# coding: utf-8

from NaoCreator.setting import Setting
Setting(nao_connected=True, debug=True, ip="192.168.0.1")

from NaoCreator.Tool.stop import normal_stop
from NaoQuest.wait_for import wait_for
from PlayerManager.player_manager import Player

Setting.naoFaceDetectionRecognition.enableRecognition(True)
Setting.naoFaceDetectionRecognition.subscribe(Setting.MEMORY_FACE, Setting.FACE_DETECTION_RECOGNITION_PERIOD, 0.0)
Setting.naoLed.on("AllLedsGreen")
Setting.naoMotion.setStiffnesses("Head", 1.0)
Setting.naoFaceTracker.startTracker()

p = Player("tristan")
wait_for(p)

normal_stop()
