import pygame as pg

from main_screen import MainScreen
from click_handler import ClickHandler
from constants import background_color

screen = pg.display.set_mode((800, 800), vsync=1)
main_screen = MainScreen(screen, background_color)
pg.display.set_caption('Ping pong')
pg.display.set_icon(pg.image.load('Icon.png'))
clock = pg.time.Clock()
ch = ClickHandler(main_screen)

FPS = 60

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
        elif event.type == pg.KEYDOWN:

            ch.key_down(event.key)
        elif event.type == pg.KEYUP:
            ch.key_up(event.key)

    ch.key_pressed(main_screen.block1, main_screen.block2)

    main_screen.redraw()
    clock.tick(FPS)
