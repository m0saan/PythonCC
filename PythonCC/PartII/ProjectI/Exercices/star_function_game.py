import pygame
from star import Star
from random import randint


def check_keydown_events(event, rocket):
    if event.key == pygame.K_RIGHT:
        rocket.moving_right = True
    if event.key == pygame.K_LEFT:
        rocket.moving_left = True
    if event.key == pygame.K_UP:
        rocket.moving_up = True
    if event.key == pygame.K_DOWN:
        rocket.moving_down = True


def check_keyup_events(event, rocket):
    if event.key == pygame.K_RIGHT:
        rocket.moving_right = False
    if event.key == pygame.K_LEFT:
        rocket.moving_left = False
    if event.key == pygame.K_UP:
        rocket.moving_up = False
    if event.key == pygame.K_DOWN:
        rocket.moving_down = False


def get_num_stars_x(r_settings, star):
    space_availibe_x = r_settings.width - 2 * star.rect.width
    num_star = int(space_availibe_x / (2 * star.rect.width))
    return num_star


def get_num_rows(r_settings, star, rocket):
    space_availibe_y = r_settings.height - 3 * \
        star.rect.height - rocket.rect_create.height
    number_rows = int(space_availibe_y / (2 * star.rect.height))
    return number_rows


def create_star(stars, screen, row_number, star_number, random_number):
    star = Star(screen)
    star.rect.x = star.rect.width + 2 * star.rect.width * star_number * random_number
    star.rect.y = star.rect.height + 2 * star.rect.height * row_number * random_number
    stars.add(star)


def create_stars(stars, r_settings, rocket, screen):
    star = Star(screen)
    num_stars_x = get_num_stars_x(r_settings, star)
    num_rows = get_num_rows(r_settings, star, rocket)
    for row_number in range(num_rows):
        for star_number in range(num_stars_x):
            random_number = randint(-5, 5)
            create_star(stars, screen, row_number, star_number, random_number)
