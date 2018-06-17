#!/usr/bin/env python
# -*- coding: utf-8 -*-

from point import Point

class Cell:
    def __init__(self, canvas, id):
        self.canvas = canvas
        self.id = id

        size = 20
        position = self.id * size
        
        self.image = self.canvas.create_rectangle(position.x, position.y, position.x + size, position.y + size, fill = "blue")
