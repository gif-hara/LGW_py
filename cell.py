#!/usr/bin/env python
# -*- coding: utf-8 -*-

from point import Point
from user_settings import *

class Cell:
    def __init__(self, canvas, id, isAlive):
        self.canvas = canvas
        self.id = id
        self.isAlive = isAlive

        size = UserSettings.cell_size()
        position = self.id * size
        
        self.image = self.canvas.create_rectangle(
            position.x,
            position.y,
            position.x + size,
            position.y + size,
            fill="blue",
            state=self.get_state(self.isAlive)
            )
        
    def set_alive(self, isAlive):
        self.canvas.itemconfig(self.image, state="hidden")
    
    def next_generation(self, cellManager):
        min = Point(self.id.x - 1, self.id.y - 1)
        for y in range(3):
            for x in range(3):
                targetId = Point(min.x + x, min.y + y)
                if targetId in cellManager.processed_cellIds:
                    continue
                adjacentNumber = cellManager.get_adjacent_number(targetId)
                isAlive = targetId in cellManager.cellIds
                if isAlive:
                    if adjacentNumber <= 1 or adjacentNumber >= 4:
                        cellManager.remove_request_ids.append(targetId)
                else:
                    if adjacentNumber == 3:
                        cellManager.create_request_ids.append(targetId)
                cellManager.processed_cellIds[targetId] = True
    
    @staticmethod
    def get_state(isAlive):
        if isAlive == True:
            return "normal"
        else:
            return "hiden"


