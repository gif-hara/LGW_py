#!/usr/bin/env python
# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod

class Application(metaclass=ABCMeta):

    _instance = None

    def __init__(self):
        pass
    
    def __new__(cls):
        if Application._instance is None:
            Application._instance = super().__new__(cls)
        return cls._instance

    @abstractmethod
    def initialize(self):
        pass
    
    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def register_schedule(self, delaySeconds, function):
        pass

    @abstractmethod
    def cancel_schedule(self, id):
        pass
