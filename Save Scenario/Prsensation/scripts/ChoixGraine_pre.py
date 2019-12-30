#coding:utf-8
                      
                      
def script(s, player=None):
    from NaoSensor.plant import Plant
    from datetime import datetime
    if not player:
        print("Error in execution of post_script \"testobj1_post\": player is None")
        return
    if not hasattr(s, "keywords"):

        s.keywords = list()
        s.kw2id = {}

    print("Exe du pre script c'est cool !!!!!!!!!!")

    current_month = datetime.now().month
    all_month = ["janvier", "fevrier", "mars", "avril", "mai", "juin", "juillet", "aout", "septembre", "octobre",
                 "novembre", "decembre"]
    month = all_month[current_month]

    list_plants = Plant.get_plantes()
    plants = ""
    for p in list_plants:
        plant = Plant(p)
        if month in plant.get_data(Plant.PLANTATION)["date"]:
            s.keywords.append(plant.get_data(Plant.NOM))
            s.keywords.append(plant.get_data(Plant.PLURIEL))
            s.kw2id[plant.get_data(Plant.PLURIEL)] = plant.get_data(Plant.NOM)
            plants += plant.get_data(Plant.NOM) + ", "
    s.question = s.question.format(plants)
