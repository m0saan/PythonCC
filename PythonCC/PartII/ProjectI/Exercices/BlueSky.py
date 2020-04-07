import pygame
import sys
from Character import Character


def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1000, 1000))
    bg_color = (0, 250, 0)
    character = Character(screen)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(bg_color)
        character.blitme()
        pygame.display.flip()


run_game()
