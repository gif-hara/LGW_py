#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
from repeated_timer import *
from preset_cell import *
import sched
from application import *

class Watch:

    def __init__(self, cellManager, offsetX, offsetY):
        self.cellManager = cellManager
        self.offsetX = offsetX
        self.offsetY = offsetY

    def start(self):
        self.update()

    def update(self):
        now = datetime.datetime.now()
        PresetCell.apply_from_string(self.cellManager, "{0:%Y/%m/%d %H:%M:%S}".format(now), 0, 0, 1)
        Application().register_schedule(1, self.update)
