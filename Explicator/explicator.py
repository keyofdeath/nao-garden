# -*- coding: utf-8 -*-

import NaoCreator.Tool.wikipediator as w
import NaoCreator.Tool.speech_move as sm
import NaoCreator.SpeechToText.nao_listen as nl
import NaoSensor.outils as o
import NaoSensor.plant as p


def get_wikipedia_answer(info):
    """
    Permet de faire la recherche sur wikipédia et de donner la première phrase de la page wikipédia
    correspondante à la question posée par l'utilisateur.
    :param info: message dit par l'utilisateur
    :return:
    """
    sm.speech_and_move(u"Désolé cette information m'est inconnue, je te redirige sur wikipédia.")
    try:
        resum = w.get_resum(info, w.FRENCH).split(".")
        sm.speech_and_move(u"Voici la réponse a ta question. {}".format(resum[0]))
    except Exception as e:
        sm.speech_and_move(u"Je n'ai pas réussi à trouver la réponse à ta question sur Wikipédia !")


def explication(msg):
    """
    Regarde si le message contient un fichier dans nos bases de données.
    :param msg: message dit par l'utilisateur
    :return:
    """
    list = p.Plant.get_plantes_obj()
    list2 = o.Outils.get_outils_obj()

    redirection = False
    #On parcourt nos deux listes à la recherche d'un mot correspondant au nom dun de nos fichiers dans nos bdd
    for item in list + list2:
        if item.get_data("nom") in msg:
            explication_obj(msg, item)
            redirection = True
            break
    #Si on ne trouve pas de mot correspondant, on renvoi sur wikipédia
    if not redirection:
        get_wikipedia_answer(msg)


def explication_obj(msg, obj):
    """
    Permet à partir d'un message et d'un type objet de parcourir le fichier trouvé de notre bdd
    :return:
    """
    sm.speech_and_move(u"redirecion sur explicator effectuée !")
    sm.speech_and_move(u"Quelles informations désires-tu sur {} {}"
                               .format(obj.get_data(obj.__class__.DETERMINANT), obj.get_data(obj.__class__.NOM)))
    list_obj = ["{}".format(key) for key in obj.data]
    sm.speech_and_move(u"Tu peux avoir des informations sur {}".format(list_obj))
    # On ecoute la question
    question = nl.nao_listen()
    # On regarde si l'info demandé est dans notre bdd et on boucle tant que l'utilisateur n'a pas dit non
    while "non" not in question:
        trouve = False
        #On récupère chaque mot dans la phrase dite par l'utilisateur
        for mot in question.split():
            if mot in list_obj:
                sm.speech_and_move(u"{} : {}".format(mot, obj.get_data(mot)))
                trouve = True
        #Si on ne trouve pas de reponse à la question, on renvoi sur wikipédia
        if not trouve:
            get_wikipedia_answer(question)

        sm.speech_and_move(u"Voudrais tu d'autres infos ? Non si tu veux quitter, "
                           u"et un autre mot clé si tu veux continuer.")
        question = nl.nao_listen()
