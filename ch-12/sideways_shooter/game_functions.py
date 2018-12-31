import sys
import pygame

def check_events(ai_settings, screen, ship):
    """Check events in game."""
    for event in pygame.event.get():
        # If quit, exit program
        if event.type == pygame.QUIT:
            sys.exit()
        # Key press events
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                ship.moving_up = True
            if event.key == pygame.K_DOWN:
                ship.moving_down = True
        elif event.type == pygame.KEYUP:
            # NOTE: Need to do this otherwise ship moves infinitely
            if event.key == pygame.K_UP:
                ship.moving_up = False
            if event.key == pygame.K_DOWN:
                ship.moving_down = False

