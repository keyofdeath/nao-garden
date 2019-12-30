#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
GNU AFFERO GENERAL PUBLIC LICENSE
    Version 3, 19 November 2007
"""
import json


class Config:
    """
    Classe permettant de récupérer la config contenue dans le fichier "naoquest_config.json" sous forme de dictionnaire
    """
    CONFIG_FILE = "naoquest_config.json"

    def __init__(self):
        """
        Construit l'objet de config du fichier "naoquest_config.json"
        """
        reader = json.load(open(Config.CONFIG_FILE), encoding="utf-8")
        self.__dict__.update(reader)
try:

    config = Config().__dict__

except Exception as e:

    pass