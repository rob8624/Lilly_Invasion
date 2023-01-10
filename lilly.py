import pygame

class Lilly:

    def __init__(self, li_game):

        self.screen = li_game.screen
        self.screen_rect = li_game.screen.get_rect()
        self.image = pygame.image.load("images/lilly.bmp")
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

        #movement flags
        self.move_right = False
        self.move_left = False

    def update(self):
        """updates lillies movement based on movement flag"""
        if self.move_right == True:
            self.rect.x += 1
        if self.move_left == True:
            self.rect.x -= 1



    def blitme(self):
        self.screen.blit(self.image, self.rect)
