from pygame import Surface
from score import ScoreTable


class MainScreen(Surface):
    def __init__(self, size):
        super().__init__(size)
        self.score = ScoreTable(self, 'red')

    def redraw(self):
        self.score.redraw()
