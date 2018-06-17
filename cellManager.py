#!/usr/bin/env python
# -*- coding: utf-8 -*-

from cell import *
from point import *

class CellManager:

    def __init__(self, canvas):
        self.canvas = canvas
        self.cells = []
        self.cellIds = {}
        self.create_request_ids = []
        self.remove_request_ids = []
        self.processed_cellIds = {}
        self.canvas.bind("<Button-1>", self.clicked_left_mouse_button)
        self.canvas.bind("<B1-Motion>", self.drag_left_mouse_button)
        self.canvas.bind("<Key>", self.any_key_down)

    def create_cell(self, id):
        cell = Cell(self.canvas, id)
        self.cells.append(cell)
        self.cellIds[id] = cell
    
    def remove_cell(self, id):
        cell = self.cellIds[id]
        cell.remove()
        self.cells.remove(cell)
        del self.cellIds[id]
    
    def remove_all_cell(self):
        for c in self.cells:
            c.remove()
        self.cells.clear()
        self.cellIds.clear()

    def contains_cell(self, id):
        return id in self.cellIds

    def next_generation(self):
        self.create_request_ids.clear()
        self.remove_request_ids.clear()
        self.processed_cellIds.clear()
        for c in self.cells:
            c.next_generation(self)
        for id in self.create_request_ids:
            self.create_cell(id)
        for id in self.remove_request_ids:
            self.remove_cell(id)

    def get_adjacent_number(self, id):
        result = 0
        min = Point(id.x - 1, id.y - 1)
        for y in range(3):
            for x in range(3):
                targetId = Point(min.x + x, min.y + y)
                if targetId == id:
                    continue
                if targetId in self.cellIds:
                    result += 1
        return result


    def clicked_left_mouse_button(self, event):
        size = UserSettings.cell_size()
        id = Point(event.x, event.y) / size
        if not self.contains_cell(id):
            self.create_cell(id)

    def drag_left_mouse_button(self, event):
        size = UserSettings.cell_size()
        id = Point(event.x, event.y) / size
        if not self.contains_cell(id):
            self.create_cell(id)
    
    def any_key_down(self, event):
        keyCode = event.char
        if keyCode == ' ':
            self.next_generation()
        if keyCode == 'q':
            self.remove_all_cell()
            
