#!/usr/bin/env python
# -*- coding: utf-8 -*-

from point import Point
from userSettings import *

class Cell:
    def __init__(self, canvas, id):
        self.canvas = canvas
        self.id = id

        size = UserSettings.cell_size()
        position = self.id * size
        
        self.image = self.canvas.create_rectangle(position.x, position.y, position.x + size, position.y + size, fill="blue")
        
    def remove(self):
        self.canvas.delete(self.image)