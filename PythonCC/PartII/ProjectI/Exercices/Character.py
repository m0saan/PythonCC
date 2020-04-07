import pygame


class Character():

    def __init__(self, screen):
        self.screen = screen
        # load and get character rect.
        self.image = pygame.image.load("img.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each character at the center of the screen.
        self.rect.center = self.screen_rect.center

    def blitme(self):
        """Draw the character. """
        self.screen.blit(self.image, self.rect)
