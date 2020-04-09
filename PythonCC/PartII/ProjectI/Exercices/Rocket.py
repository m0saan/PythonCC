import pygame


class Rocket():
    """Handle rocket drawing and movement. """

    def __init__(self, screen, settings):
        self.screen = screen
        self.r_settings = settings
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        # Load and rect Rocker image.
        self.image = pygame.image.load("img.bmp")
        self.rect_create = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Handle rocket movement.
        self.rect_create.centerx = self.screen_rect.centerx
        self.rect_create.centery = self.screen_rect.centery

        self.centerx = float(self.screen_rect.centerx)
        self.centery = float(self.screen_rect.centery)

    # Draw the rocker shape.
    def belitme(self):
        self.screen.blit(self.image, self.rect_create)

    def update_rocket(self):
        if self.moving_right and self.rect_create.right < self.screen_rect.right:
            self.centerx += self.r_settings.ship_speed_factor
        if self.moving_left and self.rect_create.left > 0:
            self.centerx -= self.r_settings.ship_speed_factor
        if self.moving_up and self.rect_create.top > 0:
            self.centery -= self.r_settings.ship_speed_factor
        if self.moving_down and self.rect_create.bottom < self.screen_rect.bottom:
            self.centery += self.r_settings.ship_speed_factor

        # Update rocket position
        self.rect_create.centerx = self.centerx
        self.rect_create.centery = self.centery
