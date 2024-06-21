from pygame import *

#konstanty aplikacie
WIN_WIDTH = 800
WIN_HEIGHT = 600
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255, 0, 0)
GREEN = (0,255,0)
FPS = 40

#trieda Player
class Player(sprite.Sprite):
    def __init__(self, x, y, width, height, speed, color):
        super().__init__()
        self.rect = draw.rect(window, color, (x, y, width, height))
        self.speed = speed
        self.color = color

    def right_move(self):
        pressed = key.get_pressed()
        if pressed[K_p] and self.rect.y > 0:
            self.rect.y -= self.speed
        if pressed[K_l] and self.rect.y < WIN_HEIGHT - self.rect.height:
            self.rect.y += self.speed
    
    def left_move(self):
        pressed = key.get_pressed()
        if pressed[K_q] and self.rect.y > 0:
            self.rect.y -= self.speed
        if pressed[K_a] and self.rect.y < WIN_HEIGHT - self.rect.height:
            self.rect.y += self.speed
         
    def draw(self):
        draw.rect(window, self.color, (self.rect))

#trieda Ball
class Ball(sprite.Sprite):
    def __init__(self, x, y, radius, speed, color):
        super().__init__()
        self.radius = radius
        self.speed = speed
        self.color = color
        self.rect = draw.circle(window, color, (x,y), radius)

    def update(self):
        pass

    def draw(self):
        draw.circle(window, self.color, (self.rect.x,self.rect.y), self.radius)


#premenne hry
run = True

#okno aplikacie
window = display.set_mode((WIN_WIDTH, WIN_HEIGHT))
display.set_caption("Ping Pong")

#casovac hry
clock = time.Clock()

#objekty hry
player1 = Player(5,100, 30, 150, 10, RED)
player2 = Player(WIN_WIDTH - 35, 100, 30, 150, 10, GREEN)
ball = Ball(WIN_WIDTH // 2, WIN_HEIGHT // 2, 10, 10, WHITE)


#herna slucka
while run:

    for e in event.get():
        if e.type == QUIT:
            run = False

    window.fill(BLACK)
    player1.left_move()
    player2.right_move()
    player1.draw()
    player2.draw()
    ball.draw()

    display.update()
    clock.tick(FPS)

quit()

