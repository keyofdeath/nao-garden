from NaoCreator.setting import Setting
Setting(nao_connected=False, debug=True, nao_quest_v="2.1", bypass_wait_for=True, load_cpt_data=False, ip="192.168.0.1")

from NaoSensor.captor_data import *
from NaoSensor.jardin import *

a = CaptorData()
C1 = a.get_data_from_csv_file(datas[0])

j = Jardin()
p = Pot(C1.get_datas())

j.reg_pot(p)

p.soil_moisture = 51
p.light = 6
p.temperature = 30
p.fertilizer = .25

print p.__dict__

pt = Plant("abricot")

print p.is_ideal_for_plant(pt)
