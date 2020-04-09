import pygame
import sys
from Rocker_settings import RocketSettings
from Rocket import Rocket
from star import Star
from pygame.sprite import Group
import star_function_game as sf


def run_game():
    """ Initialize the game and its settings."""
    pygame.init()
    r_settings = RocketSettings()
    screen = pygame.display.set_mode((r_settings.width, r_settings.height))
    pygame.display.set_caption("Rocket")
    rocket = Rocket(screen, r_settings)
    star_obj = Star(screen)
    stars = Group()
    sf.create_stars(stars, r_settings, rocket, screen)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                sf.check_keydown_events(event, rocket)
            elif event.type == pygame.KEYUP:
                sf.check_keyup_events(event, rocket)
        rocket.update_rocket()
        screen.fill(r_settings.bg_color)
        stars.draw(screen)
        rocket.belitme()

        pygame.display.flip()


run_game()
