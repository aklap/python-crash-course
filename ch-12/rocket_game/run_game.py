import sys
import pygame
from settings import Settings

def run_game():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption('Rocket Game')
    bg_color = (0, 0, 0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(settings.bg_color)
        pygame.display.flip()

run_game()