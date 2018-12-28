import sys
import pygame

def run_game():
    pygame.init()
    pygame.display.mode(1200, 800)
    pygame.display.set_caption('Rocket Game')

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()