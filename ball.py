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
        self.angle_degrees = rnd.randint(30, 150) + (rnd.randint(0, 1) * 180)
        self.angle_radians = radians(self.angle_degrees)

    def start(self):
        self.x = self.width // 2
        self.y = self.height // 2
        self.angle_degrees = rnd.randint(30, 120) + (rnd.randint(0, 1) * 180)
        self.angle_radians = radians(self.angle_degrees)

    def run(self, block1: Block, block2: Block):
        from main_screen import MainScreen
        self.main_screen: MainScreen
        if self.x + self.radius >= self.width:
            self.change_degrees_right()
        elif self.x - self.radius < 0:
            self.change_degrees_left()
        elif block1.margin + block1.height >= self.y - self.radius >= block1.margin \
                and block1.x <= self.x <= block1.x + block1.width:
            self.change_degrees_up()
        elif block2.margin <= self.main_screen.get_height() -\
                (self.y - self.radius) <= block2.margin + block2.height\
                and block2.x <= self.x <= block2.x + block2.width:
            self.change_degrees_down()
        elif self.y <= 0:
            self.start()
            self.main_screen.score.win2()
        elif self.y >= self.main_screen.get_height():
            self.start()
            self.main_screen.score.win1()

        self.x += self.speed * cos(self.angle_radians)
        self.y -= self.speed * sin(self.angle_radians)

    def change_degrees_up(self):
        if 0 <= self.angle_degrees <= 90:
            self.angle_degrees = (360 - self.angle_degrees) % 360
        elif 90 <= self.angle_degrees <= 180:
            self.angle_degrees = (180 + (180 - self.angle_degrees)) % 360
        self.angle_radians = radians(self.angle_degrees)

    def change_degrees_down(self):
        if 90 <= self.angle_degrees <= 270:
            self.angle_degrees = (180 - (self.angle_degrees - 180)) % 360
        elif 270 <= self.angle_degrees <= 360:
            self.angle_degrees = (90 - (self.angle_degrees - 270)) % 360
        self.angle_radians = radians(self.angle_degrees)

    def change_degrees_left(self):
        if 0 <= self.angle_degrees <= 180:
            self.angle_degrees = (180 - self.angle_degrees) % 360
        else:
            self.angle_degrees = (360 - (self.angle_degrees - 180)) % 360
        self.angle_radians = radians(self.angle_degrees)

    def change_degrees_right(self):
        if 0 <= self.angle_degrees <= 90:
            self.angle_degrees = (180 - self.angle_degrees) % 360
        else:
            self.angle_degrees = (360 - self.angle_degrees + 180) % 360
        self.angle_radians = radians(self.angle_degrees)

    def redraw(self, block1: Block, block2: Block):
        self.run(block1, block2)
        self.fill((0, 0, 0, 0))
        circle(self, self.color, (self.x, self.y), self.radius)
        self.main_screen.blit(self, (0, 0))
