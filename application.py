#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tkinter as tk
from cell import Cell
from cell_manager import *
from line_profiler import LineProfiler
from user_input import *

class Application:

    _instance = None

    def __init__(self):
        pass

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def initialize(self):
        self.window = tk.Tk()
        self.window.title("LGW")
        self.window.attributes("-fullscreen", True)

        self.canvas = tk.Canvas(self._instance.window, bg = "#000000")
        self.canvas.pack(fill = tk.BOTH, expand = 1)
        self.canvas.focus_set()

        self.cellManager = CellManager(self.canvas, 100, 100)
        self.userInput = UserInput(self.cellManager, self.canvas)

    def run(self):
        self.window.mainloop()
