import pygame
import sys
from settings import Settings
from lilly import Lilly

class LillyInvasion:

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width,
                                               self.settings.screen_height))
        pygame.display.set_caption(self.settings.window_caption)
        self.lilly = Lilly(self)


    def run_game(self):
        while True:
            self._check_events_()
            self._update_screen_()

    def _check_events_(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT : sys.exit()


    def _update_screen_(self):
        self.screen.fill(self.settings.bf_color)
        self.lilly.blitme()
        pygame.display.flip()


if __name__ == "__main__":
    li = LillyInvasion()
    li.run_game()

