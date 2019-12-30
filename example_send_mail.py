#!/usr/bin/env python
# -*- coding: utf-8 -*-
from NaoCreator.setting import Setting
Setting(nao_connected=True, debug=True, nao_quest_v="2.1", bypass_wait_for=False, load_cpt_data=False, ip="169.254.88.3")

from NaoCreator.Tool.speech_move import speech_and_move
from NaoCreator.SpeechToText.nao_listen import nao_listen
from NaoCreator.Tool.facebookor import send_the_post
from NaoCreator.Tool.wikipediator import get_resum, FRENCH
from NaoCreator.Tool.mailor import nao_send_mail

speech_and_move(u"Dit moi le sujet de ton mail ")
sujet = nao_listen()
speech_and_move(u"Dit moi le texte de ton mail ")
text = nao_listen()
nao_send_mail(u"mymail@orange.fr", sujet, text)
speech_and_move(u"Votre mail a bien été envoyé !")

if __name__ == '__main__':
    pass
