from pygame import Surface

from ball import Ball
from score import Score
from block import Block
from pygame.display import update as update_screen
from constants import *


class MainScreen(Surface):
    def __init__(self, main_screen: Surface, color='black'):
        super().__init__(main_screen.get_size())
        self.main_screen = main_screen
        self.background_color = color
        self.score = Score(self, color=score_color, alpha=score_alpha)
        self.block1 = Block(self, player=1, color=block1_color, size=block_size, margin=margin,
                            speed=block_speed)
        self.block2 = Block(self, player=2, color=block2_color, size=block_size, margin=margin,
                            speed=block_speed)
        self.ball = Ball(self, color=ball_color, radius=ball_radius, speed=ball_speed)

    def redraw(self):
        self.fill(self.background_color)
        self.score.redraw()
        self.block1.redraw()
        self.block2.redraw()
        self.ball.redraw(self.block1, self.block2)

        self.main_screen.blit(self, (0, 0))
        update_screen()
