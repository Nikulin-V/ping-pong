import pygame as pg
from main_screen import MainScreen


screen = pg.display.set_mode((800, 800), vsync=1)
pg.display.set_caption('Ping pong')
main_screen = MainScreen(screen.get_size())

while True:
    screen.fill('black')

    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                main_screen.score.win1()

    main_screen.redraw()
    pg.display.update()
