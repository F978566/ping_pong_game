import pyxel
from ping_pong import App


def game():
    speed_input = int(input('>>> '))
    App(150, 150, speed_input)
game()


# class App:
#     def __init__(self):
#         pyxel.init(150, 150)
#         pyxel.run(self.update, self.draw)


#     def draw(self):
#         pyxel.cls(0)
#         pyxel.text(75, 75, 'Game', 11)
    
#     def update(self):
#         if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
#             game()

# if __name__ == '__main__':
#     App()
