import pygame as pg
from random import randint

pg.init()
screen = pg.display.set_mode((500,500))
white = (255,255,255)
black = (0,0,0)
clock = pg.time.Clock()

class Cab():

    def __init__ (self, x, y):
        self.speedx = 0
        self.speedy = 0
        self.hitbox = pg.Rect(x, y, 50, 70)
        self.img = pg.image.load('C:/Users/Angela/Downloads/PY3/car.png')
        self.img = pg.transform.scale(self.img, (70, 80))

    def draw (self):
        screen.blit(self.img, (self.hitbox[0], self.hitbox[1]))


    def update (self):
        self.hitbox[0] += self.speedx
        self.hitbox[1] += self.speedy

    def edgeDetect (self):
        if self.hitbox[0]<=0 or self.hitbox[0]>=450 or self.hitbox[1]<=0 or self.hitbox[1]>=450:
            return True
        else:
            return False

class Cash():
    def __init__ (self):
        self.img = pg.image.load('C:/Users/Angela/Downloads/PY3/cash.png')
        self.hitbox = pg.Rect(randint(0, 450), randint(0, 450), 70, 70)
        self.img = pg.transform.scale(self.img, (self.hitbox[2], self.hitbox[3]))

    def respawn (self):
        self.hitbox[0] = randint(0, 450)
        self.hitbox[1] = randint(0, 450)

    def draw (self):
        screen.blit(self.img, (self.hitbox[0], self.hitbox[1]))

cab = Cab(50, 50)
cash = Cash()
score = 0
state = 1

while(state):
    pg.event.pump()

    #UPDATE
    cab.update()

    #INPUT
    keys = pg.key.get_pressed()
    if keys[pg.K_RIGHT] == 1:
        cab.speedx = 5
        cab.speedy = 0
    elif keys[pg.K_LEFT] == 1:
        cab.speedx = -5
        cab.speedy = 0
    elif keys[pg.K_UP] == 1:
        cab.speedy = -5
        cab.speedx = 0
    elif keys[pg.K_DOWN] == 1:
        cab.speedy = 5
        cab.speedx = 0

    #EVENTS
    if pg.Rect.colliderect(cab.hitbox, cash.hitbox):
        cash.respawn()
        score += 1
    if cab.edgeDetect():
        state = 0

    #DRAW
    screen.fill(white)
    cab.draw()
    cash.draw()
    pg.display.flip()

    #CLOCK
    clock.tick(60)
