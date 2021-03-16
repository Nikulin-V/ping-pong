import pygame as pg
from block import Block


class ClickHandler:
    def __init__(self, window_width):
        self.window_width = window_width

        self.left1_key = pg.K_a
        self.right1_key = pg.K_d
        self.left2_key = pg.K_LEFT
        self.right2_key = pg.K_RIGHT

        self.left1_key_pressed = False
        self.right1_key_pressed = False
        self.left2_key_pressed = False
        self.right2_key_pressed = False

    def key_down(self, key):
        if key == self.left1_key:
            self.left1_key_pressed = True
        elif key == self.right1_key:
            self.right1_key_pressed = True
        elif key == self.left2_key:
            self.left2_key_pressed = True
        elif key == self.right2_key:
            self.right2_key_pressed = True

    def key_up(self, key):
        if key == self.left1_key:
            self.left1_key_pressed = False
        elif key == self.right1_key:
            self.right1_key_pressed = False
        elif key == self.left2_key:
            self.left2_key_pressed = False
        elif key == self.right2_key:
            self.right2_key_pressed = False

    def key_pressed(self, block1: Block, block2: Block):
        w = self.window_width
        if self.left1_key_pressed and block1.x > 0:
            block1.go_left()
        if self.right1_key_pressed and block1.x + block1.width < w:
            block1.go_right()
        if self.left2_key_pressed and block2.x > 0:
            block2.go_left()
        if self.right2_key_pressed and block2.x + block2.width < w:
            block2.go_right()
