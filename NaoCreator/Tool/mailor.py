#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
GNU AFFERO GENERAL PUBLIC LICENSE
    Version 3, 19 November 2007
"""
import smtplib
from NaoCreator.setting import *
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import NaoCreator.Tool.speech_move as sm
import tkSimpleDialog
import re


def get_user_mail():
    """
    Récupère le mail de l'utilisateur devant nao
    :return: le mail entrer par l'utilistaeur
    """
    sm.speech_and_move(u"Peux-tu entrer ton adresse mail ?")
    email_re = re.compile(
        r"(^[-!#$%&'*+/=?^_`{}|~0-9A-Z]+(\.[-!#$%&'*+/=?^_`{}|~0-9A-Z]+)*"  # dot-atom
        r'|^"([\001-\010\013\014\016-\037!#-\[\]-\177]|\\[\001-011\013\014\016-\177])*"'  # quoted-string
        r')@(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?$', re.IGNORECASE)  # domain

    while True:
        try:
            mail = tkSimpleDialog.askstring('Email', 'Adresse mail')
            # si le mail est correct
            if email_re.search(mail):
                return mail
            else:
                sm.speech_and_move(u"L'adresse mail que tu as entrée n'est pas valide")
        except Exception as e:
            print e


def nao_send_mail(mail, subject, text):
    """
    Envoie un mail
    :param mail: adresse mail de destination
    :param subject: Objet du mail
    :param text: texte du mail
    :return: 
    """

    msg = MIMEMultipart()

    msg['From'] = Setting.mail_adresse
    msg['To'] = mail
    msg['Subject'] = subject

    msg.attach(MIMEText(text, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(Setting.mail_adresse, Setting.password)
    server.sendmail(Setting.mail_adresse, mail, msg.as_string())
    server.quit()

if __name__ == '__main__':
    pass
