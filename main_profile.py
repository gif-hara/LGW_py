#!/usr/bin/env python
# -*- coding: utf-8 -*-

from application import Application
from line_profiler import LineProfiler
from cell import *
from cell_manager import *

def main():
    app = Application()
    app.initialize()
    for y in range(20):
        for x in range(20):
            app.cellManager.set_alive(x, y, True)
    app.cellManager.next_generation()
    app.window.quit()

profile = LineProfiler()
profile.add_module(Cell)
profile.add_module(CellManager)
profile.add_function(main)
profile.runcall(main)
profile.print_stats()
