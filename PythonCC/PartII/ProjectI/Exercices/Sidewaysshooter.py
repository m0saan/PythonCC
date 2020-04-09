import pygame
import sys
from Rocker_settings import RocketSettings as Settings
from shooter import Shooter
from pygame.sprite import Group
from shooter_bullet import Bullet


def update_bullet(bullets):
    bullets.update()


def run_game():
    pygame.init()
    sideway_shooter = Settings()
    screen = pygame.display.set_mode((
        sideway_shooter.width, sideway_shooter.height))
    pygame.display.set_caption("__Hjira__")
    shooter = Shooter(screen)
    bullets = Group()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    shooter.moving_up = True
                if event.key == pygame.K_DOWN:
                    shooter.moving_down = True
                elif event.key == pygame.K_SPACE:
                    new_bullet = Bullet(screen, sideway_shooter, shooter)
                    bullets.add(new_bullet)
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    shooter.moving_up = False
                if event.key == pygame.K_DOWN:
                    shooter.moving_down = False
        shooter.update()
        screen.fill(sideway_shooter.bg_color)
        shooter.belitme()
        bullets.update()
        for bullet in bullets.sprites():
            bullet.draw_bullet()
        for bullet in bullets.copy():
            if bullet.rect.top <= 0:
                bullets.remove(bullet)
        print(len(bullets))
        pygame.display.flip()


run_game()
