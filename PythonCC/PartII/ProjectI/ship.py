import pygame


class Ship():
    def __init__(self, screen, settings):
        """Initialize the ship and set its starting position."""
        self.screen = screen
        self.moving_right = False
        self.moving_left = False
        self.ai_settings = settings

        # Load the ship image and get its rect.
        self.image = pygame.image.load('./images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Store a decimal value for the ship's center.
        self.center = float(self.rect.centerx)

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """ Update the ship's position based on the movement flag. """
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += 2 * self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= 2 * self.ai_settings.ship_speed_factor

        # Update rect object for self.center
        self.rect.centerx = self.center