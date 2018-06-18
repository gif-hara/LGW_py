#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tkinter as tk
from cell import Cell
from cell_manager import *
from line_profiler import LineProfiler
from user_input import *
import math
from application import Application

class ApplicationTkinter(Application):

    def initialize(self):
        self.window = tk.Tk()
        self.window.title("LGW")
        self.window.attributes("-fullscreen", True)

        self.canvas = tk.Canvas(self._instance.window, bg = "#000000")
        self.canvas.pack(fill = tk.BOTH, expand = 1)
        self.canvas.focus_set()

        width = self.window.winfo_width()
        height = self.window.winfo_height()
        size = UserSettings.cell_size()
        self.cellManager = CellManager(self.canvas, math.floor(width / size), math.floor(height / size))
        self.userInput = UserInput(self.cellManager, self.canvas)

    def run(self):
        self.window.mainloop()