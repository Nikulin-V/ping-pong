from pygame import Surface
from pygame.font import Font, init as font_init

font_init()


class Score:
    def __init__(self, main_screen: Surface, color='white', alpha=50):
        self.color = color
        self.alpha = alpha
        self.font = Font(None, 100)
        self.score1 = 0
        self.score2 = 0
        self.main_screen = main_screen
        self.x = None
        self.y = None

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

        width, height = self.main_screen.get_size()
        self.x = width // 2 - text.get_width() // 2 - 2
        self.y = height // 2 - text.get_height() // 2 - 3
        # 2 и 3 - погрешность pygame, найдено подбором
        text.set_alpha(self.alpha)
        self.main_screen.blit(text, (self.x, self.y))
