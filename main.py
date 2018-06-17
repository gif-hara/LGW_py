#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tkinter as tk
from cell import Cell
from point import Point
from cellManager import *
from line_profiler import LineProfiler

profiler = LineProfiler()

def main():
    root = tk.Tk()
    root.title("LGW")
    root.attributes("-fullscreen", True)

    # def input_key(event):
    #     print("input = {}".format(repr(event.char)))

    canvas = tk.Canvas(root, bg = "#000000")
    canvas.pack(fill = tk.BOTH, expand = 1)
    # canvas.bind("<Key>", input_key)
    canvas.focus_set()

    cellManager = CellManager(canvas)
    
    for y in range(20):
        for x in range(20):
            cellManager.create_cell(Point(x, y))
    cellManager.next_generation()

    # root.mainloop()
    root.quit()

profiler.add_module(Cell)
profiler.add_module(Point)
profiler.add_module(CellManager)
profiler.add_function(main)

profiler.runcall(main)

profiler.print_stats()

#main()