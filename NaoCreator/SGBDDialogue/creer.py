#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
GNU AFFERO GENERAL PUBLIC LICENSE
    Version 3, 19 November 2007
"""
__author__ = 'no-code-team'
from random import randint
import re
import codecs


Confirmation = "Confirmation"
Demande = "Demande"
Humour = "Humour"
Instruction = "Instruction"
MotsUtiles = "Mots Utiles"
Reponse = "Reponse"
DicoVide = {}


def _remplace(balise, ligne):
    """
    Fonction qui remplace les balises par les valeurs souhaitées
    :param balise: dictionnaire contenant les valeurs à mettre dans les balises
    :param ligne: string qui contient des balises
    :return: la ligne donnée avec les valeurs dans les balises
    """

    tab_ligne = re.split("<|>", ligne)
    for i in range(len(tab_ligne)):
        tab_ligne[i] = tab_ligne[i].strip()  # on enlève les espaces
        try:
            val_balise = balise[tab_ligne[i]]  # on récupère les valeurs du dico
        except Exception as e:
            print(e)
        else:
            tab_ligne[i] = str(val_balise)

    return ' '.join(tab_ligne)


def _get_phrase(type_phrase, num_phrase):
    """
    Fonction qui récupère les phrase demandées et donne un tableau de celles-ci
    :param type_phrase: type de phrases à chercher
    :param num_phrase: tableau des phrases à chercher dans le fichier
    :return: le tableau des phrases trouvées
    """
    f = codecs.open("NaoCreator/SGBDDialogue/fichiers/{}".format(type_phrase), 'r', 'utf-8')
    tab_result = []

    # Num ligne, ligne du fichier en str
    for line in f:  # on parcourt notre fichier
        id_phrase = int(line.split(']')[0])  # on recupère le numéro de la ligne dans le fichier
        if id_phrase in num_phrase:  # on compare aux numéros voulus
            tab_result.append(line)  # on récupère la ligne

    f.close()
    return tab_result


class Creer(object):
    def __init__(self, type_phrase, balise, *num_phrase):
        """
        Cette classe va permettre de récupérer un choix de phrase et renvoyer une phrase au hasard parmi celles
        demandées
        :param type_phrase: type_phrase de phrase à récupérer
        :param balise: Valeur des balises à changer sous la forme d'un dico
        :param num_phrase: tableau des numéros de phrase à trouver
        :return: None
        """
        self.tab_phrase = _get_phrase(type_phrase, sorted(num_phrase))
        self.balise = balise

    def out(self):
        """
        Fonction qui renvoie une phrase aléatoirement parmis celles choisies
        :return:Une phrase choisie aléatoirement parmis les phrases choisies
        """
        i = randint(0, len(self.tab_phrase)-1)
        phrase = self.tab_phrase[i]
        phrase = phrase.split(']')[1]

        if '>' in phrase:
            phrase = _remplace(self.balise, phrase)

        phrase.replace("\n", "")
        return phrase

    def set_balise(self, balise):
        """
        Fonction qui modifie l'attribut balise et remplace les balises par leurs valeurs
        :param balise: attribut en question
        :return:
        """
        self.balise = balise
