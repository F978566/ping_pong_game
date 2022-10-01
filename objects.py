import pyxel


class Racket:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w = 8
        self.h = 40


    def draw(self):
        pyxel.blt(self.x, self.y, 0, 8, 0, self.w, self.h)


class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w = 8
        self.h = 8


    def draw(self):
        pyxel.blt(self.x, self.y, 1, 8, 0, self.w, self.h)