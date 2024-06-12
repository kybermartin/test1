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
        self.rect = draw.circle(window, color, (x,y), radius)
        self.speed = speed
        self.color = color
        self.radius = radius
        self.directionX = 1
        self.directionY = 1

    def move(self):
        if self.rect.y < 0 or self.rect.y > (WIN_HEIGHT - (2 * self.radius)):
            self.directionY = -1 * self.directionY 
         
        self.rect.x += self.speed
        self.rect.y += self.speed * self.directionY 

    def draw(self):
        draw.circle(window, self.color, self.rect.center, self.radius) 


#premenne hry
run = True

#okno aplikacie
window = display.set_mode((WIN_WIDTH, WIN_HEIGHT))
display.set_caption("Ping Pong")

#casovac hry
clock = time.Clock()

#objekty hry
player1 = Player(5,100, 20, 150, 10, RED)
player2 = Player(WIN_WIDTH - 25, 100, 20, 150, 10, GREEN)
ball = Ball(WIN_WIDTH // 2, WIN_HEIGHT // 2, 10, 5, WHITE)

#herna slucka
while run:

    for e in event.get():
        if e.type == QUIT:
            run = False

    window.fill(BLACK)
    player1.left_move()
    player2.right_move()
    ball.move()
    player1.draw()
    player2.draw()
    ball.draw()

    display.update()
    clock.tick(FPS)

quit()

