"""A module for game functions."""

import sys
import pygame
from bullet import Bullet


def check_events(ai_settings, screen, ship, bullets):
    """Check events in game."""
    for event in pygame.event.get():
        # If quit, exit program
        if event.type == pygame.QUIT:
            sys.exit()
        # Key press events
        elif event.type == pygame.KEYDOWN:
            # Move ship up
            if event.key == pygame.K_UP:
                ship.moving_up = True
            # Move ship down
            if event.key == pygame.K_DOWN:
                ship.moving_down = True
            # Fire a bullet
            if event.key == pygame.K_SPACE:
                fire_bullet(ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            # NOTE: Need to do this otherwise ship moves infinitely
            if event.key == pygame.K_UP:
                ship.moving_up = False
            if event.key == pygame.K_DOWN:
                ship.moving_down = False


def fire_bullet(ai_settings, screen, ship, bullets):
    """Fire bullet from ship."""
    # If bullet
    if len(bullets) < ai_settings.bullet_limit:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


# NOTE: Why isn't this in bullet.py? Why does gf need to know this?
def update_bullets(bullets, ai_settings):
    """Update the position of bullets."""
    bullets.update()

    for bullet in bullets.copy():
        if bullet.rect.right >= ai_settings.screen_width:
            bullets.remove(bullet)


def update_screen(ai_settings, screen, ship, bullets):
    """Update the screen, re-draw and re-render."""
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # Draw ship
    screen.blit(ship.image, ship.rect)
    # Re-render the lastest version of the window
    pygame.display.flip()  # Update window
