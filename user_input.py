#!/usr/bin/env python
# -*- coding: utf-8 -*-

from cell_manager import *
from repeated_timer import *
from user_settings import *
import math

class UserInput:
    def __init__(self, cellManager, canvas):
        self.cellManager = cellManager
        self.canvas = canvas
        self.canvas.bind("<Button-1>", self.clicked_left_mouse_button)
        self.canvas.bind("<B1-Motion>", self.drag_left_mouse_button)
        self.canvas.bind("<Key>", self.any_key_down)
        self.repeat_next_generation = None

    def clicked_left_mouse_button(self, event):
        size = UserSettings.cell_size()
        x = math.floor(event.x / size)
        y = math.floor(event.y / size)
        if self.cellManager.get_alive(x, y) == False:
            self.cellManager.set_alive(x, y, True)

    def drag_left_mouse_button(self, event):
        size = UserSettings.cell_size()
        x = math.floor(event.x / size)
        y = math.floor(event.y / size)
        if self.cellManager.get_alive(x, y) == False:
            self.cellManager.set_alive(x, y, True)
    
    def any_key_down(self, event):
        keyCode = event.char
        if keyCode == ' ':
            self.cellManager.next_generation()
        if keyCode == 'q':
            self.cellManager.remove_all_cell()
        if keyCode == 'w':
            for y in range(100):
                for x in range(50):
                    self.cellManager.create_cell(Point(x, y))
        if keyCode == 'z' and self.repeat_next_generation is None:
            self.repeat_next_generation = RepeatedTimer(UserSettings.interval(), self.cellManager.next_generation)
            self.repeat_next_generation.start()
        if keyCode == 'x' and self.repeat_next_generation is not None:
            self.repeat_next_generation.cancel()
            del self.repeat_next_generation
            self.repeat_next_generation = None




