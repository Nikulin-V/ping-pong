from pygame import Surface, SRCALPHA
from pygame.draw import rect


class Block(Surface):
    def __init__(self, main_screen: Surface, player, color='white',
                 size=(50, 10), margin=30, speed=7):
        self.width, self.height = size
        super().__init__((main_screen.get_width(), self.height), SRCALPHA)
        self.main_screen = main_screen
        self.color = color
        self.margin = margin
        self.speed = speed
        self.player = player
        self.x = main_screen.get_width() // 2 - self.width // 2
        self.y = 0

    def go_right(self):
        self.x += self.speed
        self.redraw()

    def go_left(self):
        self.x -= self.speed
        self.redraw()

    def redraw(self):
        from main_screen import MainScreen
        self.main_screen: MainScreen
        self.fill(self.main_screen.background_color)

        rect(self, self.color, (self.x, self.y, self.width, self.height))

        blit_margin = self.margin if self.player == 1 \
            else self.main_screen.get_height() - self.margin
        self.main_screen.blit(self, (0, blit_margin))
