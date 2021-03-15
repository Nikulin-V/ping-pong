import pygame as pg


class Ball:
    def __init__(self, color, radius, size):
        self.ball_color = color
        self.ball_radius = radius
        self.width, self.height = size
        self.ball_speed = 10

    def start(self):

