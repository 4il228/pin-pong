from pygame import *

WIN_WIDTH = 900
WIN_HEIGHT = 800
FPS = 60

display.set_caption('Ping-pong')
window = display.set_mode((WIN_WIDTH, WIN_HEIGHT))

timer = time.Clock()

font.init() 

game = True

while game:

    for e in event.get():
        if e.type == QUIT:
            game = False

    window.fill((50, 64, 112))
    display.update()
    timer.tick(FPS)
