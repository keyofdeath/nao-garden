#!/usr/bin/env python
# -*- coding: utf-8 -*-
from NaoSensor.captor_data import *

a = CaptorData()
a.get_data_from_csv_file(datas[0])
print(a.data)

if __name__ == '__main__':
    pass

