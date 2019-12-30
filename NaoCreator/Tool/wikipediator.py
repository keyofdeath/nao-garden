#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
GNU AFFERO GENERAL PUBLIC LICENSE
    Version 3, 19 November 2007
"""
import wikipedia


FRENCH = "fr"
ENGLISH = "en"


def get_resum(word_to_search, language):
    """
    Fonction qui renvoie le résumé du wikipedia du mot cherché
    :param word_to_search: Mot à chercher
    :param language: Lanque de recherche
    :return: Le résumé trouvé en texte brute
    """

    wikipedia.set_lang(language)
    return wikipedia.summary(word_to_search)
