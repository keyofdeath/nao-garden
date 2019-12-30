#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
GNU AFFERO GENERAL PUBLIC LICENSE
    Version 3, 19 November 2007
"""

try:
    from NaoCreator.SpeechToText.nao_listen import nao_listen
except Exception as e:
    pass


def sentence_keywords(phrase, mots_clefs):
    return list(set(phrase.split()) & set(mots_clefs))

# retro-compa
mots_clefs_dans_phrase = sentence_keywords


def nao_key_word_recognition(*key_word):
    """
    Fonction qui renvoie le mots entendus
    :param key_word: Liste des mots-clefs attendus
    :return: Le mot clef entendu par l'utilisateur
    """

    msg = nao_listen().lower()

    for key in key_word:

        if key in msg:
            return key

    # si on n'a rien trouvé
    return ""

