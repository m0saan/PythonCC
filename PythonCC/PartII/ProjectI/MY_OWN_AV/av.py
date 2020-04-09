import pygame
import sys
from pygame.sprite import Group
from settings import Settings
from bullet import Bullet
from ship import Ship
from alien import Alien
import gf


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((
        ai_settings.sc_width, ai_settings.sc_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(screen, ai_settings)
    bullets = Group()
    aliens = Group()
    bullet = Bullet(screen, ai_settings, ship)
    alien = Alien(screen, ai_settings)
    gf.create_fleet(aliens, screen, ai_settings, ship)
    while True:
        for event in pygame.event.get():
            gf.check_events(event, ship, bullets, screen, ai_settings)
        ship.update()
        gf.update_screen(screen, bullets, ai_settings, ship, aliens, alien)
        gf.update_aliens(aliens, ai_settings)
        bullets.update()
        pygame.display.flip()


run_game()
