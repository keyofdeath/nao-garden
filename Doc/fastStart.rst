Démarage rapide
===============

Démarrer et utiliser Nao scénario en 5 Steps !

******
Step 1
******

    Installer tout ce qui est nécessaire pour démarrer NaoProject. Pour plus d'informations, voir la rubrique "Installation de Nao project".

******
Step 2
******

    Il est nécessaire de bénéficier d'une connexion Internet ! Il est donc recommandé d'être connecté à Internet via un câble filaire, et d'être connecté à NAO via sa WiFi.

    .. image:: /image/wifi_Nao_Pc.png

    **ou**

    Il est aussi possible d'être relié à Internet via sa carte wifi, et d'être relié à NAO avec un câble filaire.

    .. image:: /image/wifi_Internet_PC.png


    **IMPORTANT** Pour mettre l'adresse ip de Nao il faut éditer le fichier **main.py** ligne Setting(nao_connected=True, debug=True, nao_quest_v="2.1", ip="192.168.0.1") en modifiant l'attribut **ip**

******
Step 3
******

    Une fois Nao allumé, éxécutez le script de premier démmarage a l'aide de la commande "python First_start_script.py"

******
Step 4
******

    Maintenant, il est possible de démarrer le script Python à l'aide de la commande "Python main.py".
    Le script devrait démarrer sans retourner d'erreur.
    Si tout se passe bien, les yeux de Nao devraient devenir verts, puis il devrait parler.

******
Step 5
******

    Suivez ensuite les instructions du :download:`Pdf Dialogue Nao <_static/Nao_aide.pdf>`. Pour plus d'informations, veuillez consulter la rubrique "Description du code NAO Project".

*******
To Stop
*******

    **Pour arreter le programme proprement il faut appuyer sur le pied droit de Nao pendant la recherche de visage.**
    **Si vous avez dû arrêter le programme d'une autre façon, il faut exécuter le script stopNao.py.**