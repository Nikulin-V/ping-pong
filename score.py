import pygame as pg
from pygame import Surface
from pygame.font import Font

pg.font.init()


class ScoreTable:
    def __init__(self, main_screen: Surface, color):
        self.score1 = 0
        self.score2 = 0
        self.color = color
        width, height = main_screen.get_size()
        self.x, self.y = width // 2, height // 2
        self.main_screen = main_screen
        self.font = Font(None, 100)
        self.redraw()

    def redraw(self):
        self.main_screen.blit(self.font.render(f'{self.score1} : {self.score2}', True, self.color),
                              (self.x - 70, self.y - 50, self.x + 100, self.y + 100))

    def win1(self):
        self.score1 += 1
        self.redraw()

    def win2(self):
        self.score2 += 1
        self.redraw()
