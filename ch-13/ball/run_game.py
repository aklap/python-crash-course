import pygame
import game_functions as gf


def run_game():
    """Run game."""
    # Initialize game
    pygame.init()
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
        for event in pygame.event.get():
            gf.check_events(event, person)
        # Update sprite positions
        gf.update_person(person)
        gf.update_ball(ball, person)
        # Re-render screen
        gf.update_screen(screen, ball, person)

# Run our game loop
run_game()
