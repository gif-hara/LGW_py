#!/usr/bin/env python
# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod

class Application(metaclass=ABCMeta):

    _instance = None

    def __init__(self):
        pass
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    @abstractmethod
    def initialize(self):
        pass
    
    @abstractmethod
    def run(self):
        pass
