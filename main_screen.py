from pygame import Surface
from score import Score
from pygame.display import update as update_screen


class MainScreen(Surface):
    def __init__(self, main_screen: Surface):
        super().__init__(main_screen.get_size())
        self.main_screen = main_screen
        self.score = Score(self, 'red')

    def redraw(self):
        self.fill('black')
        self.score.redraw()
        self.main_screen.blit(self, (0, 0))

        update_screen()
