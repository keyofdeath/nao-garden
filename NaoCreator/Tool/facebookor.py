#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
GNU AFFERO GENERAL PUBLIC LICENSE
    Version 3, 19 November 2007
"""

import facebook


def send_the_post(msg):
    """
    Ecrit un post facebook
    :param msg: le message que l'on veut écrire
    :return: 
    """

    # Fill in the values noted in previous steps here
    cfg = {
        "page_id": "1536198983059262",
        "access_token": "EAAFAEV2SX8MBAD47SOzllYZCujhRqd1HKZB7UZC71ZCOpKOJ7GI3U251gXv4zTFSnoZAoPsNHAm3jRBsZBJX5OZBGQ2UHkp97tYapvDKyp67SeUdieSUSNvuozsnguaGjklNDi5yRETKChATZAG4QE8OAxllll2mp1wZD"
    }

    api = get_api(cfg)
    status = api.put_wall_post(msg)


def get_api(cfg):
    """
    récupère l'accès à l'api facebook
    :param cfg: dico qui contient l'id de la page facebook et le token d'accès
    :return:
    """
    graph = facebook.GraphAPI(cfg['access_token'])
    # Get page token to post as the page. You can skip
    # the following if you want to post as yourself.
    resp = graph.get_object('me/accounts')
    page_access_token = None
    for page in resp['data']:
        if page['id'] == cfg['page_id']:
            page_access_token = page['access_token']
    graph = facebook.GraphAPI(page_access_token)
    return graph
    # You can also skip the above if you get a page token:
    # http://stackoverflow.com/questions/8231877/facebook-access-token-for-pages
    # and make that long-lived token as in Step 3

if __name__ == "__main__":
  send_the_post("Hello this is a test ! ┏(:|])┛┗(:))┓┗(:D)┛┏(8|)┓")

