import pygame
import game_functions as gf
from settings import Settings

def run_game():
    """Run game."""
    # Initialize game
    pygame.init()
    # Initialize settings
    settings = Settings()
    # Create window
    screen = pygame.display.set_mode((1200, 800))
    # Create caption
    pygame.display.set_caption('Catch Game')
    # Generate a ball
    ball = gf.create_ball(screen)
    # Create a person
    person = gf.create_person(screen)

    # Run loop
    while True:
        gf.check_events(person)
        # Update sprite positions
        gf.update_person(person)
        gf.update_ball(ball, person, settings)
        # Re-render screen
        gf.update_screen(screen, ball, person)

# Run our game loop
run_game()
