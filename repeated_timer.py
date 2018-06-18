#!/usr/bin/env python
# -*- coding: utf-8 -*-

import signal
import time

class RepeatedTimer(Timer):
    def __init__(self, interval, function, args=[], kwargs={}):
        Timer.__init__(self, interval, function, args, kwargs)
        self.thread = None
        self.funcion = function

    def run(self):
        self.thread = Timer(self.interval, self.run)
        self.thread.start()
        self.funcion(*self.args, *self.kwargs)

    def cancel(self):
        if self.thread not None:
            self.thread.cancel()
            self.thread.join()
            del self.thread