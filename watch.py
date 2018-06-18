#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
from repeated_timer import *
from preset_cell import *
import sched
from application import *
import math

class Watch:

    def __init__(self, cellManager):
        self.cellManager = cellManager

    def start(self):
        self.update()

    def update(self):
        now = datetime.datetime.now()
        formatNow0 = "{0:%Y/%m/%d}".format(now)
        formatNow1 = "{0:%H:%M:%S}".format(now)
        space = 1
        charX = PresetCell.char_x()
        charY = PresetCell.char_y()
        offsetX0 = math.floor((self.cellManager.width - len(formatNow0) * charX) / 2)
        offsetX1 = math.floor((self.cellManager.width - len(formatNow1) * charX) / 2)
        offsetY0 = math.floor((self.cellManager.height - charY) / 2) - 3
        offsetY1 = math.floor((self.cellManager.height - charY) / 2) + 3
        
        PresetCell.apply_from_string(self.cellManager, formatNow0, offsetX0 - 1, offsetY0, space)
        PresetCell.apply_from_string(self.cellManager, formatNow1, offsetX1, offsetY1, space)
        Application().register_schedule(1, self.update)
