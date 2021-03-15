import pygame as pg


screen = pg.display.set_mode((800, 800), vsync=1)
pg.display.set_caption('Ping pong')


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()

    screen.fill('black')
