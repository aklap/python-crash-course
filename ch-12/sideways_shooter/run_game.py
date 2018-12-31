import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    pygame.init()  # Initialize game
    # Settings
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))  # Create window
    ship = Ship(ai_settings, screen)

    # Check events
    while True:
        # Check events
        gf.check_events(ai_settings, screen, ship)
        # Fill background color
        screen.fill(ai_settings.bg_color)
        # Update ship
        ship.update()
        # Draw objects in window
        screen.blit(ship.image, ship.rect)
        # Re-render the lastest version of the window
        pygame.display.flip() # Update window

# Run game loop
run_game()