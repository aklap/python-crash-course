import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    """Run game loop."""
    pygame.init()  # Initialize game
    # Settings
    ai_settings = Settings()
    # Create window
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    # Create ship
    ship = Ship(ai_settings, screen)
    # Needs to be imported from the sprite module of pygame
    bullets = Group()

    # Event loop
    while True:
        # Check events
        gf.check_events(ai_settings, screen, ship, bullets)
        # Fill background color
        screen.fill(ai_settings.bg_color)
        # Update ship
        ship.update()
        # Update bullets
        gf.update_bullets(bullets, ai_settings)
        # Draw objects in window
        gf.update_screen(ai_settings, screen, ship, bullets)


# Run game loop
run_game()
