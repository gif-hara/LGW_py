class Point:
    def __init__(self):
        self.x = 0
        self.y = 0

    def __init__(self, x, y):
        self.set(x, y)

    def set(self, x, y):
        self.x = x
        self.y = y
