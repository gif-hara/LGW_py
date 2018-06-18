#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
from repeated_timer import *
from preset_cell import *
import sched
from application import *
import math
from user_settings import *

class Watch:

    def __init__(self, backgroundCellManager, foregroundCellManager):
        self.backgroundCellManager = backgroundCellManager
        self.foregroundCellManager = foregroundCellManager

    def start(self):
        self.update()

    def update(self):
        self.update_cell_manager(self.backgroundCellManager, False)
        self.update_cell_manager(self.foregroundCellManager, True)
        Application().register_schedule(1, self.update)

    def update_cell_manager(self, cellManager, ignoreRemoveCell):
        now = datetime.datetime.now()
        formatNow0 = "{0:%Y/%m/%d}".format(now)
        formatNow1 = "{0:%H:%M:%S}".format(now)
        space = 1
        charX = PresetCell.char_x()
        charY = PresetCell.char_y()

        offsetX0 = math.floor((cellManager.width - len(formatNow0) * charX) / 2) - 1 + UserSettings.offset_x_watch()
        offsetX1 = math.floor((cellManager.width - len(formatNow1) * charX) / 2) + UserSettings.offset_x_watch()
        offsetY0 = math.floor((cellManager.height - charY) / 2) - 3
        offsetY1 = math.floor((cellManager.height - charY) / 2) + 3
        PresetCell.apply_from_string(cellManager, formatNow0, offsetX0, offsetY0, space, ignoreRemoveCell)
        PresetCell.apply_from_string(cellManager, formatNow1, offsetX1, offsetY1, space, ignoreRemoveCell)
