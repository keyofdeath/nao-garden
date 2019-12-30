#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
GNU AFFERO GENERAL PUBLIC LICENSE
    Version 3, 19 November 2007
"""
import codecs


def say(*args):
    print("[NAO] \"" + u" ".join([codecs.decode(arg, "utf-8") for arg in args]) + "\"")


def wait(*args):
    pass


class post:
    # Pour enlever l'erreur de Pycharm...
    def __init__(self):
        pass

    @staticmethod
    def say(args):
        say(args)
