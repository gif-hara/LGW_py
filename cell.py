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
        
    @staticmethod
    def get_state(isAlive):
        if isAlive == True:
            return "normal"
        else:
            return "hidden"


