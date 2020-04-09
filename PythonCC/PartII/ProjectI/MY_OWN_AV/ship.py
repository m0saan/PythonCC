import pygame


class Ship():
    """A class that represents the ship creation and properties. """

    def __init__(self, screen, ai_settings):
        self.screen = screen
        self.moving_right = False
        self.moving_left = False
        self.ai_settings = ai_settings

        # load and draw the ship.
        self.image = pygame.image.load("./images/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # Position the ship in the bottom center.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Create a var to hold exact value
        self.x = float(self.rect.centerx)

    def draw_ship(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.ai_settings.move_speed_factor
        if self.moving_left and self.rect.left >= 0:
            self.x -= self.ai_settings.move_speed_factor

        self.rect.centerx = self.x
