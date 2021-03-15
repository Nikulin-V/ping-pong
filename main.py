import pygame as pg

from main_screen import MainScreen

screen = pg.display.set_mode((800, 800), vsync=1)
main_screen = MainScreen(screen)
pg.display.set_caption('Ping pong')

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()

    main_screen.redraw()
