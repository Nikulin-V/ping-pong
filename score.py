from pygame import Surface
from pygame.font import Font, init as font_init
font_init()


class Score:
    def __init__(self, main_screen: Surface, color):
        self.color = color
        self.font = Font(None, 100)
        self.score1 = 0
        self.score2 = 0
        self.main_screen = main_screen
        width, height = main_screen.get_size()
        self.x = width // 2 - 50
        self.y = height // 2 - 60

    def start(self):
        self.score1 = 0
        self.score2 = 0

    def win1(self):
        self.score1 += 1
        from main_screen import MainScreen
        self.main_screen: MainScreen
        self.main_screen.redraw()

    def win2(self):
        self.score2 += 1
        from main_screen import MainScreen
        self.main_screen: MainScreen
        self.main_screen.redraw()

    def redraw(self):
        text = self.font.render(f'{self.score1} : {self.score2}', True, self.color)
        text.set_alpha(50)
        self.main_screen.blit(text, (self.x, self.y))
