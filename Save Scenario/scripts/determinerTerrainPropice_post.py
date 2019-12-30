#coding:utf-8


def script(s, player=None):
  from NaoQuest.objective import Objective
  from NaoCreator.setting import Setting
  from NaoSensor.plant import Plant
  from NaoQuest.scenario import Scenario
  import NaoCreator.Tool.speech_move as sm

  print "il se lance ou pas ce fdp"

  if not player:
    Setting.error("Error in execution of post_script of objective \"determienrTerrainPropice\": player is None")
    return

  jardin = player.current_scenario.jardin
  plante_ideale = Plant()
  plante_ideale.data["valeursIdeales"] = {
  "soil_moisture": {
  "min": 50.0,
  "max": 80.0
  },
  "light": {
  "min": 5.0,
  "max": 8.0
  },
  "temperature": {
  "min": 20.0,
  "max": 50.0
  },
  "fertilizer": {
  "min": 0.2,
  "max": 0.4
  }
  }

  pots_ideals = [(p, i) for p, i in zip(jardin.pots, range(1, len(jardin.pots) + 1)) if p.is_ideal_for_plant(plante_ideale)]
  player.current_scenario.pots_ideals = pots_ideals

  if not pots_ideals:
    sm.speech_and_move("Il semblerait qu'aucuns des pots que tu as enregistrés présentent des caractéristiques idéales. Assure toi de trouver un terrain lumineux, riche et humide et relance le scénario.")
    player.current_scenario = Scenario("terrainPropice")
    print("Redémarrage du Scénario \"Terrain Propice\" !")
    return

  texte = "Selon mes données, il semblerait que les pots. "
  for t in pots_ideals:
    texte += str(t[1]) + ", "
  texte += "présentent des caractéristiques intéressantes pour ton jardin."
  sm.speech_and_move(texte)
