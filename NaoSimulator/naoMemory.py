#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
GNU AFFERO GENERAL PUBLIC LICENSE
    Version 3, 19 November 2007
"""
from NaoSimulator.get_mic_input import *


def getData(*arg):
    return 1 if record() else 0
