import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """ A class to represent a single alien. """

    def __init__(self, screen, ai_settings):
        self.screen = screen
        self.ai_settings = ai_settings
        super().__init__()

        # load and draw alien.
        self.image = pygame.image.load("./images/alien.bmp")
        self.rect = self.image.get_rect()

        # position the alien shape.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # store exact position for alien.
        self.x = float(self.rect.x)

    def blitme(self):
        """Draw the alien at its current location."""
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.x += (self.ai_settings.alien_speed_factor *
                   self.ai_settings.fleet_direction)
        self.rect.x = self.x

    def check_alien_edge(self):
        self.screen_rect = self.screen.get_rect()
        if self.rect.right >= self.screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
