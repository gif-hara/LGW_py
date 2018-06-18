#!/usr/bin/env python
# -*- coding: utf-8 -*-

class PresetCell:

    @staticmethod
    def apply_from_char(cellManager, char, offsetX, offsetY):
        PresetCell._apply(PresetCell._dictionary[char], cellManager, offsetX, offsetY)

    @staticmethod
    def apply_from_string(cellManager, string, offsetX, offsetY, space):
        for char in string:
            PresetCell._apply(PresetCell._dictionary[char], cellManager, offsetX, offsetY)
            offsetX += 3 + space

    @staticmethod
    def _apply(charTuple, cellManager, offsetX, offsetY):
        posX = offsetX
        posY = offsetY
        for y in charTuple:
            for x in y:
                if x == 1:
                    cellManager.set_alive(posX, posY, True)
                else:
                    cellManager.set_alive(posX, posY, False)
                posX += 1
            posY += 1
            posX = offsetX

    @staticmethod
    def char_x():
        return 3
    
    @staticmethod
    def char_y():
        return 5

    _num0 = (
        (1,1,1),
        (1,0,1),
        (1,0,1),
        (1,0,1),
        (1,1,1),
    )
    _num1 = (
        (0,1,0),
        (0,1,0),
        (0,1,0),
        (0,1,0),
        (0,1,0),
    )
    _num2 = (
        (1,1,1),
        (0,0,1),
        (1,1,1),
        (1,0,0),
        (1,1,1),
    )
    _num3 = (
        (1,1,1),
        (0,0,1),
        (1,1,1),
        (0,0,1),
        (1,1,1),
    )
    _num4 = (
        (1,0,1),
        (1,0,1),
        (1,1,1),
        (0,0,1),
        (0,0,1),
    )
    _num5 = (
        (1,1,1),
        (1,0,0),
        (1,1,1),
        (0,0,1),
        (1,1,1),
    )
    _num6 = (
        (1,1,1),
        (1,0,0),
        (1,1,1),
        (1,0,1),
        (1,1,1),
    )
    _num7 = (
        (1,1,1),
        (0,0,1),
        (0,0,1),
        (0,0,1),
        (0,0,1),
    )
    _num8 = (
        (1,1,1),
        (1,0,1),
        (1,1,1),
        (1,0,1),
        (1,1,1),
    )
    _num9 = (
        (1,1,1),
        (1,0,1),
        (1,1,1),
        (0,0,1),
        (1,1,1),
    )
    _slash = (
        (0,0,1),
        (0,1,0),
        (0,1,0),
        (0,1,0),
        (1,0,0),
    )
    _colon = (
        (0,0,0),
        (0,1,0),
        (0,0,0),
        (0,1,0),
        (0,0,0),
    )
    _space = (
        (0,0,0),
        (0,0,0),
        (0,0,0),
        (0,0,0),
        (0,0,0),
    )

    _dictionary = {
        '0':_num0,
        '1':_num1,
        '2':_num2,
        '3':_num3,
        '4':_num4,
        '5':_num5,
        '6':_num6,
        '7':_num7,
        '8':_num8,
        '9':_num9,
        '/':_slash,
        ':':_colon,
        ' ':_space,
    }