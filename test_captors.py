from NaoCreator.setting import Setting
Setting(nao_connected=False, debug=True, nao_quest_v="2.1", bypass_wait_for=True, load_cpt_data=False)

from NaoSensor.captor_data import *

print cpt_giselle.data[0][CaptorData.TEMPERATURE]
