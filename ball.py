import pygame as pg
import random as rnd

from pygame import Surface


class Ball:
    def __init__(self, main_screen: Surface, color, radius):
        self.ball_color = color
        self.ball_radius = radius
        self.main_screen = main_screen
        self.width, self.height = main_screen.get_size()
        self.x_coord = self.width // 2
        self.y_coord = self.height // 2
        self.ball_speed = 10
        self.angle = rnd.randint(16, 75)
        self.quarter = rnd.randint(1, 5)

    def start(self):
        self.x_coord = self.width // 2
        self.y_coord = self.height // 2
        self.angle = rnd.randint(16, 75)
        self.quarter = rnd.randint(1, 5)

    def get_coord(self):
        pass
