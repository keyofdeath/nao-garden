#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
GNU AFFERO GENERAL PUBLIC LICENSE
    Version 3, 19 November 2007
Script a utiliser quand on allume Nao la première fois
"""
from NaoCreator.setting import *


def delete_face_db():
    """
    Vide la base de données des visages
    :return:
    """
    result = Setting.naoFaceDetectionRecognition.clearDatabase()
    print "Supression data visage ", result

if __name__ == '__main__':
    delete_face_db()
