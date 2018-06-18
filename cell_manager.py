#!/usr/bin/env python
# -*- coding: utf-8 -*-

from cell import *
from threading import Lock

class CellManager:

    def __init__(self, canvas, width, height, color):
        cells = []
        for y in range(height):
            for x in range(width):
                cells.append(Cell(canvas, x, y, UserSettings.cell_size(), False, color))
        self.cells = tuple(cells)
        self.create_requests = []
        self.remove_requests = []
        self.processed_cellIds = {}
        self.width = width
        self.height = height
        self.lock = Lock()
    
    def remove_all_cell(self):
        for c in self.cells:
            c.set_alive(False)
    
    def set_alive(self, x, y, isAlive):
        self.cells[x + y * self.width].set_alive(isAlive)

    def get_alive(self, x, y):
        return self.cells[x + y * self.width].isAlive

    def next_generation(self):
        with self.lock:
            self.create_requests.clear()
            self.remove_requests.clear()
            self.processed_cellIds.clear()
            for c in self.cells:
                c.next_generation(self)
            for c in self.create_requests:
                c.set_alive(True)
            for c in self.remove_requests:
                c.set_alive(False)

    def get_adjacent_number(self, posX, posY):
        result = 0
        minX = posX - 1
        minY = posY - 1
        for y in range(3):
            for x in range(3):
                targetX = minX + x
                targetY = minY + y
                if posX == targetX and posY == targetY:
                    continue
                if targetX >= 0 and targetX < self.width and targetY >= 0 and targetY < self.height:
                    if self.cells[targetX + targetY * self.width].isAlive == True:
                        result += 1
        return result
