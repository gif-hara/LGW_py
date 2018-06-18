#!/usr/bin/env python
# -*- coding: utf-8 -*-

from user_settings import *

class Cell:
    def __init__(self, canvas, x, y, size, isAlive):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.isAlive = isAlive

        posX = x * size
        posY = y * size
        
        self.image = self.canvas.create_rectangle(
            posX,
            posY,
            posX + size,
            posY + size,
            fill="blue",
            state=self.get_state(self.isAlive)
            )
        
    def set_alive(self, isAlive):
        self.isAlive = isAlive
        self.canvas.itemconfig(self.image, state=self.get_state(self.isAlive))

    def next_generation(self, cellManager):
        if self.isAlive == False:
            return
        minX = self.x - 1
        minY = self.y - 1
        for y in range(3):
            for x in range(3):
                targetX = minX + x
                targetY = minY + y
                if targetX >= 0 and targetX < cellManager.width and targetY >= 0 and targetY < cellManager.height:
                    adjacentNumber = cellManager.get_adjacent_number(targetX, targetY)
                    cell = cellManager.cells[targetX + targetY * cellManager.width]
                    if cell.isAlive == True and adjacentNumber <= 1 or adjacentNumber >= 4:
                        cellManager.remove_requests.append(cell)
                    elif cell.isAlive == False and adjacentNumber == 3:
                        cellManager.create_requests.append(cell)
        
    @staticmethod
    def get_state(isAlive):
        if isAlive == True:
            return "normal"
        else:
            return "hidden"


