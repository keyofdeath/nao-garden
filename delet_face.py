#!/usr/bin/env python
# -*- coding: utf-8 -*-
from NaoCreator.setting import *
from NaoCreator.Tool.delete_face_db import delete_face_db
Setting(nao_connected=True, debug=True, nao_quest_v="2.1", ip="169.254.88.3")

if __name__ == '__main__':
    delete_face_db()
