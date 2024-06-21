from pygame import *

font.init()

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
        self.x_speed = speed
        self.y_speed = speed
        self.color = color
        self.rect = draw.circle(window, color, (x,y), radius)

    def update(self):
        if self.rect.y - self.radius < 0 or self.rect.y + self.radius > WIN_HEIGHT:
            self.y_speed *= -1

        self.rect.x += self.x_speed
        self.rect.y += self.y_speed  

    def draw(self):
        draw.circle(window, self.color, (self.rect.x,self.rect.y), self.radius)

# trieda kolizii
class CollideManager():
    def __init__(self, player1, player2, ball):
        #kolizie
        self.player1 = player1
        self.player2 = player2
        self.ball = ball


    def update(self):
        if sprite.collide_rect(self.ball, self.player2):
            ball.x_speed *= -1
            ball.rect.right = player2.rect.left
            
        if sprite.collide_rect(self.ball, self.player1):
            ball.x_speed *= -1
            ball.rect.left = player1.rect.right
            
        if ball.rect.x > WIN_WIDTH:            
            pass
        if ball.rect.x < 0:
            pass

#premenne hry
run = True

#okno aplikacie
window = display.set_mode((WIN_WIDTH, WIN_HEIGHT))
display.set_caption("Ping Pong")

#casovac hry
clock = time.Clock()

#objekty hry
player1 = Player(5,100, 30, 150, 10, RED)
player2 = Player(WIN_WIDTH - 35, WIN_HEIGHT - 200, 30, 150, 10, GREEN)
ball = Ball(WIN_WIDTH // 2, WIN_HEIGHT // 2, 10, 4, WHITE)
collide = CollideManager(player1, player2, ball)

#herna slucka
while run:

    for e in event.get():
        if e.type == QUIT:
            run = False

    window.fill(BLACK)
    collide.update()
    player1.left_move()
    player2.right_move()
    ball.update()
    player1.draw()
    player2.draw()
    
    ball.draw()

    display.update()
    clock.tick(FPS)

quit()

