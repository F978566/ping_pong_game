import pyxel
from objects import Racket, Ball
from random import randint


class App:
    def __init__(self, window_w, window_h, acceleration):
        pyxel.init(window_w, window_h)
        pyxel.load('assets_for_ping_pong/assets.pyxres')
        self.x1 = 0
        self.y1 = 60
        self.speed_racket = 4

        self.x2 = window_w - 8
        self.y2 = 60

        self.x_ball = 50
        self.y_ball = 50
        self.speed_ball = 1
        self.gravity = 0

        self.points_first_player = 0
        self.points_second_player = 0

        self.acceleration = acceleration

        pyxel.run(self.update, self.draw)


    def update(self):
        self.racket1 = Racket(self.x1, self.y1)
        self.racket2 = Racket(self.x2, self.y2)

        self.ball = Ball(self.x_ball, self.y_ball)
        self.x_ball -= self.speed_ball
        self.y_ball += self.gravity

        self.move_ball()
        self.move_racket_player()
        self.move_second_player()
        # self.move_racket()
        self.death()


    def draw(self):
        pyxel.cls(0)
        pyxel.text(65, 10, str(self.points_first_player), 11)
        pyxel.text(75, 10, '|', 11)
        pyxel.text(85, 10, str(self.points_second_player), 11)
        self.racket1.draw()
        self.racket2.draw()
        self.ball.draw()


    def move_ball(self):
        if self.x1 + 8 == self.x_ball and self.y1 <= self.y_ball+4 and self.y1 + 40 > self.y_ball+4:
            self.speed_ball = -1 - self.acceleration
            self.gravity = randint(-2, 2)
        elif self.x2 - 8 == self.x_ball and self.y2 <= self.y_ball+4 and self.y2 + 40 > self.y_ball+4:
            self.speed_ball = 1 + self.acceleration
            self.gravity = randint(-2, 2)

            self.speed_ball = -1 - self.acceleration
            self.gravity = 1
        elif self.y_ball <= 0 and self.speed_ball > 0:
            self.speed_ball = 1 + self.acceleration
            self.gravity = 1
        elif self.y_ball >= 140 and self.speed_ball < 0:
            self.speed_ball = -1 - self.acceleration
            self.gravity = -1
        elif self.y_ball >= 140 and self.speed_ball > 0:
            self.speed_ball = 1 + self.acceleration
            self.gravity = -1

    def death(self):
        if self.x_ball < 0:
            self.points_second_player += 1
            self.x_ball = 50
            self.y_ball = 50
            self.speed_ball = 1
            self.gravity = 0
            self.y1, self.y2 = 50, 50
        elif self.x_ball > 150:
            self.points_first_player += 1
            self.x_ball = 50
            self.y_ball = 50
            self.speed_ball = 1
            self.gravity = 0
            self.y1, self.y2 = 50, 50


    def move_racket_player(self):
        if pyxel.btn(pyxel.KEY_W):
            self.y1 -= self.speed_racket
        elif pyxel.btn(pyxel.KEY_S):
            self.y1 += self.speed_racket
    
    def move_racket(self):
        if pyxel.btn(pyxel.KEY_W):
            self.y2 -= self.speed_racket
        elif pyxel.btn(pyxel.KEY_S):
            self.y2 += self.speed_racket

    def move_second_player(self):
        if pyxel.btn(pyxel.KEY_UP):
            self.y2 -= self.speed_racket
        elif pyxel.btn(pyxel.KEY_DOWN):
            self.y2 += self.speed_racket


if __name__ == '__main__':
    App(150, 150, int(input()))