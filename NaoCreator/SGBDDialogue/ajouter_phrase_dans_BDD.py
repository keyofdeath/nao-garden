#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
GNU AFFERO GENERAL PUBLIC LICENSE
    Version 3, 19 November 2007
"""
from __future__ import unicode_literals
import creer as Dg
import codecs
import sys


def get_file_name():
    """
    Demande à l'utilisateur dans quel fichier il souhaite ajouter une phrase
    :return: le nom du fichier que l'utilisateur a choisi
    """
    file_name = raw_input("Dans quel fichier veux-tu ajouter une phrase ? (<Confirmation>, <Demande>, ...) ")
    while file_name not in [Dg.Confirmation, Dg.Demande, Dg.Humour, Dg.Instruction, Dg.MotsUtiles, Dg.Reponse]:
        print "Nom du fichier invalide"
        file_name = raw_input("Dans quel fichier veux-tu ajouter une phrase ? (<Confirmation>, <Demande>, ...) ")
    return file_name


def add_sentence(file_name):
    """
    Ajoute la phrase entrée par l'utilisateur
    :param file_name: le fichier dans lequel il faut insérer la phrase
    :return:
    """
    sentence = raw_input("Quelle phrase veux-tu ajouter ? ").decode(sys.stdin.encoding)

    f = codecs.open("fichiers/{}".format(file_name), 'r', 'utf-8')

    max_id = 0
    for line in f:
        id_phrase = int(line.split(']')[0])  # on recupère le numéro de la ligne dans le fichier
        if id_phrase > max_id:
            max_id = id_phrase
    max_id += 1

    f.close()
    f = codecs.open("fichiers/{}".format(file_name), 'a', 'utf-8')
    sentence = u"\n{}]{}".format(max_id, sentence)
    f.write(sentence)
    f.close()

    print "Phrase ajoutée avec l'id {}\n".format(max_id)


if __name__ == '__main__':

    file_name = get_file_name()
    add_sentence(file_name)

    answer = raw_input("Continuer ? <n/c/m> (n: non / c: oui, changer de fichier / m: oui, même dossier) ")
    while answer != 'n':
        if answer == 'c':
            file_name = get_file_name()
            add_sentence(file_name)
        if answer == 'm':
            add_sentence(file_name)
        answer = raw_input("Continuer ? <n/c/m> (n: non / c: oui, changer de fichier / m: oui, même dossier) ")
