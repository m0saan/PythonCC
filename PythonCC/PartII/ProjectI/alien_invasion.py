import pygame
from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    ship = Ship(screen, ai_settings)
    pygame.display.set_caption("Alien Invasion")
    while True:
        gf.check_events(ship)
        # Move the ship to the right.
        ship.update()
        gf.update_screen(ai_settings, ship, screen)
        # Make the most recently drawn screen visible.
        pygame.display.flip()


run_game()
