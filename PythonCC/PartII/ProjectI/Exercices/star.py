import pygame
from pygame.sprite import Sprite


class Star(Sprite):
    """ A class to represent a single star in space. """

    def __init__(self, screen):
        self.screen = screen
        super().__init__()

        # Load and get rect form image.
        self.image = pygame.image.load("img.bmp")
        self.rect = self.image.get_rect()

        # Postion the star rect.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Draw the star
        def draw_me(self):
            self.screen.blit(self.image, self.rect)
