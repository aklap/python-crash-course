import pygame  # NOTE: Allows us to build our game
from pygame.sprite import Group
from settings import Settings
from game_stats import Stats as GameStats
from ship import Ship
import game_functions as gf
from button import Button
from target import Target

def run_game():
    """Initialize game, create window object."""
    pygame.init()  # NOTE: Initialize a pygame instance.
    ai_settings = Settings()
    # Screen settings.
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    # Add title to window.
    pygame.display.set_caption('Alien Invasion')
    # Draw button.
    play_button = Button(ai_settings, screen, "Play")
    # Make a ship.
    ship = Ship(ai_settings, screen)
    # Make bullets.
    bullets = Group()
    # Make target
    target = Target(ai_settings, screen)

    # Create the fleet of .
    # gf.create_fleet(ai_settings, screen, ship)

    # Initalize stats for a new game
    stats = GameStats(ai_settings)

    # Start the run loop for our game.
    while True:
        gf.check_events(ai_settings, screen, ship, bullets, stats, play_button)
        if stats.game_active:
            ship.update()
            target.update()
            gf.update_target(ai_settings, screen, target, bullets)
            gf.update_bullets(ai_settings, screen, ship, bullets, target, stats)
        gf.update_screen(ai_settings, screen, ship, bullets, stats, play_button, target)

# Run the game :)
run_game()
