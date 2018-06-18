#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tkinter as tk
from cell import Cell
from cell_manager import *
from line_profiler import LineProfiler
from user_input import *
import math
from application import Application
from watch import *

class ApplicationTkinter(Application):

    def initialize(self):
        self.window = tk.Tk()
        self.window.title("LGW")
        self.window.attributes("-fullscreen", True)

        self.canvas = tk.Canvas(self._instance.window, bg = "#000000")
        self.canvas.pack(fill = tk.BOTH, expand = 1)
        self.canvas.focus_set()

        # width, heightが正しく取得出来ないので強制更新する
        self.window.update_idletasks()

        size = UserSettings.cell_size()
        width = math.floor(self.window.winfo_width() / size)
        height = math.floor(self.window.winfo_height() / size)

        self.backgroundCellManager = CellManager(self.canvas, width, height, "blue")
        backgroundWatch = Watch(self.backgroundCellManager, 0, 0)

        self.foregroundCellManager = CellManager(self.canvas, width, height, "green")
        foregroundWatch = Watch(self.foregroundCellManager, 0, 0)

        backgroundWatch.start()
        foregroundWatch.start()

        self.userInput = UserInput(self.backgroundCellManager, self.canvas)

    def run(self):
        self.window.mainloop()

    def schedule(self, delay, function):
        self.window.after(delay, function)
