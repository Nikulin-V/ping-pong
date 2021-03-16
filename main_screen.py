from pygame import Surface
from score import Score
from block import Block
from pygame.display import update as update_screen


class MainScreen(Surface):
    def __init__(self, main_screen: Surface, background_color='black'):
        super().__init__(main_screen.get_size())
        self.main_screen = main_screen
        self.background_color = background_color
        self.score = Score(self)
        self.block1 = Block(self, player=1)
        self.block2 = Block(self, player=2)

    def redraw(self):
        self.fill(self.background_color)
        self.score.redraw()
        self.block1.redraw()
        self.block2.redraw()

        self.main_screen.blit(self, (0, 0))
        update_screen()
