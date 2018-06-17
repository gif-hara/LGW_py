#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tkinter as tk
from cell import Cell
from point import Point
from cellManager import *

root = tk.Tk()
root.title("LGW")
#root.attributes("-fullscreen", True)

def input_key(event):
    print("input = {}".format(repr(event.char)))

canvas = tk.Canvas(root, bg = "#000000")
canvas.pack(fill = tk.BOTH, expand = 1)
canvas.bind("<Key>", input_key)
canvas.focus_set()

cellManager = CellManager(canvas)

root.mainloop()
