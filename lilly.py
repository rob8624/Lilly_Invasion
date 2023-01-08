import pygame

class Lilly:

    def __init__(self, li_game):

        self.screen = li_game.screen
        self.screen_rect = li_game.screen.get_rect()
        self.image = pygame.image.load("images/lilly.bmp")
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        self.screen.blit(self.image, self.rect)
