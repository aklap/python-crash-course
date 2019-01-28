import pygame
import sys
from drop import Drop
from random import randint

def update_screen(screen, drops):
    """Redraw screen with updated raindrops."""
    screen.fill((0, 0, 0))
    drops.draw(screen)
    pygame.display.flip()


def check_events():
    """Check if user wants to end game."""
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                sys.exit()

def create_raindrops(screen, number_rows, number_drops, drops):
    """Generate all raindrops."""
    for row in range(number_rows):
            for drop_num in range(number_drops):
                # Create new instance of Drop
                drop = Drop(screen)
                drop_width = drop.rect.width
                drop.x = drop_width + (2 * drop_width * drop_num)
                drop.rect.x = drop.x
                drop.rect.y = drop.rect.height + (2 * drop.rect.height * row)
                drops.add(drop)

def rain_drops(screen, drops):
    # Update raindrops position.
        for drop in drops.sprites():
            drop.rect.y += randint(1, 10)
            # If drop is below bottom of screen, remove it and don't update it.
            if drop.rect.bottom >= screen.get_rect().height:
                drop.rect.y = 0
