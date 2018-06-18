#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tkinter as tk
from cell import Cell
from point import Point
from cell_manager import *
from line_profiler import LineProfiler
from user_input import *

class Application:

    _instance = None

    window = None

    def __init__(self):
        pass

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def initialize(self):
        self._instance.window = tk.Tk()
        self._instance.window.title("LGW")
        self._instance.window.attributes("-fullscreen", True)

        canvas = tk.Canvas(self._instance.window, bg = "#000000")
        canvas.pack(fill = tk.BOTH, expand = 1)
        canvas.focus_set()

        cellManager = CellManager(canvas, 100, 100)
        userInput = UserInput(cellManager, canvas)

    def run(self):
        self._instance.window.mainloop()
