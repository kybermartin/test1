from pygame import *

#konstanty aplikacie
WIN_WIDTH = 800
WIN_HEIGHT = 600
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255, 0, 0)
GREEN = (0,255,0)
FPS = 40

#premenne hry
run = True

#okno aplikacie
window = display.set_mode((WIN_WIDTH, WIN_HEIGHT))
display.set_caption("Ping Pong")

#casovac hry
clock = time.Clock()

#herna slucka
while run:

    for e in event.get():
        if e.type == QUIT:
            run = False

    display.update()
    clock.tick(FPS)

quit()

