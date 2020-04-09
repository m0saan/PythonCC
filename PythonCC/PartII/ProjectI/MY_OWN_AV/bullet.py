import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """A class handles bullets."""

    def __init__(self, screen, ai_settings, ship):
        self.screen = screen
        self.ai_settings = ai_settings
        super().__init__()

        # Create bullet and position it.
        self.rect = pygame.Rect(
            0, 0, ai_settings.bullet_width, ai_settings.bullet_hight)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.y = float(self.rect.y)

    def update(self):
        self.y -= self.ai_settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.ai_settings.bullet_color, self.rect)
