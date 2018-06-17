#!/usr/bin/env python
# -*- coding: utf-8 -*-

from cell import *

class CellManager:

    def __init__(self, canvas):
        self.canvas = canvas
        self.cells = []
        self.cellIds = []
        self.canvas.bind("<Button-1>", self.clicked_left_mouse_button)
        self.canvas.bind("<B1-Motion>", self.drag_left_mouse_button)

    def create_cell(self, id):
        cell = Cell(self.canvas, id)
        self.cells.append(cell)
        self.cellIds.append(id.__hash__())
    
    def remove_cell(self, id):
        index = self.cellIds.index(id.__hash__())
        self.cells.pop(index).remove()
        del self.cellIds[index]

    def contains_cell(self, id):
        return id.__hash__() in self.cellIds

    def clicked_left_mouse_button(self, event):
        size = UserSettings.cell_size()
        id = Point(event.x, event.y) / size
        if self.contains_cell(id):
            self.remove_cell(id)
        else:
            self.create_cell(id)

    def drag_left_mouse_button(self, event):
        size = UserSettings.cell_size()
        id = Point(event.x, event.y) / size
        if not self.contains_cell(id):
            self.create_cell(id)
