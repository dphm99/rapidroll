import pygame as pg

# Thông số game
pg.init()

WIDTH = 576
HEIGHT = 1024
FPS = 60
TITLE = 'Rapid Roll'
HS_File = 'highscore.txt'
black = (0, 0, 0)

# Starting platform
PlAT_LIST = [(WIDTH / 2, HEIGHT - 165),
             (WIDTH / 3, HEIGHT/2),
             (125,HEIGHT-350),
             (350,HEIGHT*2/3),
             (800,162)]

STAR_LIST = [(145, HEIGHT - 350),
             (320,HEIGHT*3/5),
             (423,140)]

CRACK_LIST = [(WIDTH / 4, HEIGHT - 60),
             (WIDTH / 1.5, HEIGHT/3),
             (160,HEIGHT-310),
             ]
# Hệ số chuyển động
Ball_acc = 0.75
Ball_gra = 1
# Gia tốc
Ball_fric = -0.30



