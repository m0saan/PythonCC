import pygame


class Shooter():

    def __init__(self, screen):
        self.screen = screen
        self.moving_up = False
        self.moving_down = False

        # Load and get rect from image.
        self.image = pygame.image.load("img.bmp")
        self.rect = self.image.get_rect()
        self.rect_screen = self.screen.get_rect()

        # Set the rect posiiton
        self.rect.bottom = self.rect_screen.bottom
        self.rect.left = self.rect_screen.left

    def belitme(self):
        # Draw the shape
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_up:
            self.rect.bottom -= 2
        if self.moving_down:
            self.rect.bottom += 1
