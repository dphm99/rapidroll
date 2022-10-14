# Các lớp đối tượng trong game

from thongsogame import *

# Vecto Vận tốc
vec = pg.math.Vector2

class Ball(pg.sprite.Sprite):
    def __init__(self,game):
        self.game = game
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load('assets/sprites/ball.png')
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, 100)
        self.pos = vec(WIDTH/2, 100)
        self.vel = vec(0,0)
        self.acc = vec(0,0)


    def update(self):
        self.acc = vec(0,Ball_gra)
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.acc.x = -Ball_acc
        if keys[pg.K_RIGHT]:
            self.acc.x = Ball_acc
        # Áp dụng gia tốc vật lý
        self.acc += self.vel * Ball_fric

        # Hệ số chuyển động
        self.vel += self.acc
        self.pos += self.vel

        # Giới hạn phạm vi di chuyển
        if self.pos.x > WIDTH - 17:
            self.pos.x = WIDTH - 17
        if self.pos.x < 0 + 17:
            self.pos.x = 0 + 17

        self.rect.midbottom = self.pos

class Plat(pg.sprite.Sprite):
    def __init__(self, x,y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load('assets/sprites/green.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speedy = 2

    def update(self):
        self.rect.y -= self.speedy

class Star(pg.sprite.Sprite):
    def __init__(self, x,y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load('assets/sprites/star.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speedy = 2

    def update(self):
        self.rect.y -= self.speedy

class Crack(pg.sprite.Sprite):
    def __init__(self,x,y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load('assets/sprites/crack.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speedcr = 2

    def update(self):
        self.rect.y -= self.speedcr

class Heart(pg.sprite.Sprite):
    def __init__(self, x,y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load('assets/sprites/heart.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speedy = 2

    def update(self):
        self.rect.y -= self.speedy

class Nail(pg.sprite.Sprite):
    def __init__(self, x,y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load('assets/sprites/nails.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
