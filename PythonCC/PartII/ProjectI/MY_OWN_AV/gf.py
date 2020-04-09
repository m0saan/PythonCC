import pygame
import sys
from bullet import Bullet
from alien import Alien


def check_keydown_events(event, ship, bullets, screen, ai_settings):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    if event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        create_bullet(ship, bullets, screen, ai_settings)
    elif event.key == pygame.K_ESCAPE:
        sys.exit()


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(event, ship, bullets, screen, ai_settings):
    if event.type == pygame.QUIT:
        sys.exit()
    elif event.type == pygame.KEYDOWN:
        check_keydown_events(event, ship, bullets, screen, ai_settings)
    elif event.type == pygame.KEYUP:
        check_keyup_events(event, ship)


def update_screen(screen, bullets, ai_settings, ship, aliens, alien):
    screen.fill(ai_settings.bg_color)
    ship.draw_ship()

    # draw bullets.
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    # Delete bullet
    for bullet in bullets.copy():
        if bullet.rect.top <= 0:
            bullets.remove(bullet)

    aliens.draw(screen)


def update_aliens(aliens, ai_settings):
    aliens.update()
    check_fleet_edges(aliens, ai_settings)


def create_bullet(ship, bullets, screen, ai_settings):
    new_bullet = Bullet(screen, ai_settings, ship)
    bullets.add(new_bullet)


def count_aliens_avail(alien, screen, ai_settings):
    availibe_space_x = ai_settings.sc_width - 2 * alien.rect.width
    number_of_aliens = int(availibe_space_x / (2 * alien.rect.width))
    return number_of_aliens


def count_rows_avail(alien, screen, ai_settings, ship):
    availibe_space_y = ai_settings.sc_height - \
        3 * alien.rect.height - ship.rect.height
    num_aliens_y = int(availibe_space_y / (2 * alien.rect.height))
    return num_aliens_y


def create_alien(aliens, screen, ai_settings, ship, alien_x, alien_y):
    alien = Alien(screen, ai_settings)
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    alien.x = alien_width + 2 * alien_width * alien_x
    alien.rect.x = alien.x
    alien.rect.y = alien_height + 2 * alien_height * alien_y
    aliens.add(alien)


def create_fleet(aliens, screen, ai_settings, ship):
    alien = Alien(screen, ai_settings)
    num_aliens_x = count_aliens_avail(alien, screen, ai_settings)
    num_aliens_y = count_rows_avail(alien, screen, ai_settings, ship)
    for alien_y in range(num_aliens_y):
        for alien_x in range(num_aliens_x):
            create_alien(aliens, screen, ai_settings, ship, alien_x, alien_y)


def change_fleet_direction(aliens, ai_settings):
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= (-1)


def check_fleet_edges(aliens, ai_settings):
    for alien in aliens.sprites():
        if alien.check_alien_edge():
            change_fleet_direction(aliens, ai_settings)
            break
