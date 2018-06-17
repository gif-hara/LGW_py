#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Point:
    def __init__(self):
        self.x = 0
        self.y = 0

    def __init__(self, x, y):
        self.set(x, y)

    def __add__(self, other):
        return Point(self.x + other.x. self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Point(self.x * other, self.y * other)

    def set(self, x, y):
        self.x = x
        self.y = y
