import pygame
from pygame.sprite import Group
from drop import Drop
import game_functions as gf


def run_game():
    """Run raindrop game."""
    # Initialize game
    pygame.init()
    # Create window
    screen = pygame.display.set_mode((1200, 800))
    # Add caption to window
    pygame.display.set_caption('Raindrop Game')
    # Create collection of Drop sprites
    drops = Group()

    # Create a single drop
    drop = Drop(screen)
    drop_width = drop.rect.width
    drop_height = drop.rect.height

    # Available room for drops width wise
    available_space_x = 1200 - (drop_width * 2)
    # How many stars can fit width-wise on screen
    number_drops = int(available_space_x / (2 * drop_width))
    # Available space for rows of stars
    available_space_y = (800 - drop_height)
    number_rows = int(available_space_y / (2 * drop_height))

    gf.create_raindrops(screen, number_rows, number_drops, drops)

    # Game loop
    while True:
        gf.check_events()
        gf.rain_drops(screen, drops)
        gf.update_screen(screen, drops)

run_game()
