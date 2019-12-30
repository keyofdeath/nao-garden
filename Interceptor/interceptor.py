#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
GNU AFFERO GENERAL PUBLIC LICENSE
    Version 3, 19 November 2007
"""
import Explicator.explicator as e


def typemsg(msg):
    """
    Fonction qui analyse le type du message, et reconnait si c'est une question ou une exclamation.
    Si c'est une question, on renvoi sur explicator.
    :param msg: Message envoyé à interceptor, en tolower()
    :return: un booléen, vrai si le msg est une question et faux si ce n'est pas reconnu comme une question
    """
    # Notre tableau de mot cle qui peuvent etre dans une question
    mot_cle = {"pourquoi", "quand", "quoi", "comment", "ça va", "et toi", "qu'est-ce", "où", "informations", "qui"}
    if mot_cle.intersection(msg.split(" ")):
        e.explication(msg)
        return True
    return False
