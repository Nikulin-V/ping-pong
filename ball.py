from pygame import Surface, SRCALPHA
from pygame.draw import circle
from math import sin, cos, radians
import random as rnd
from block import Block


class Ball(Surface):
    def __init__(self, main_screen: Surface, color='white', radius=7, speed=5):
        super().__init__(main_screen.get_size(), SRCALPHA)
        self.color = color
        self.radius = radius
        self.main_screen = main_screen
        self.width, self.height = main_screen.get_size()
        self.speed = speed
        self.x = self.width // 2
        self.y = self.height // 2
        self.angle_degrees = rnd.randint(16, 75) * rnd.randint(1, 4)
        self.angle_radians = radians(self.angle_degrees)

    def start(self):
        self.x = self.width // 2
        self.y = self.height // 2
        self.angle_degrees = rnd.randint(15, 75) * rnd.randint(1, 4)
        self.angle_radians = radians(self.angle_degrees)

    def run(self, block1: Block, block2: Block):
        if self.x + self.radius > self.width:
            self.change_degrees(180)
        elif self.x - self.radius < 0:
            self.change_degrees(90)
        elif self.y - self.radius == block1.y and block1.x <= self.x <= block1.x + block1.width:
            self.change_degrees(90)
        self.x += self.speed * cos(self.angle_radians)
        self.y -= self.speed * sin(self.angle_radians)

    def change_degrees(self, deg):
        self.angle_degrees = abs(self.angle_degrees - deg) % 360
        self.angle_radians = radians(self.angle_degrees)

    def redraw(self, block1: Block, block2: Block):
        self.run(block1, block2)
        print(self.angle_degrees)
        self.fill((0, 0, 0, 0))
        circle(self, self.color, (self.x, self.y), self.radius)
        self.main_screen.blit(self, (0, 0))
