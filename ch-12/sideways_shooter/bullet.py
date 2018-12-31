"""Class Bullet."""

import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Base class representing a bullet."""

    def __init__(self, ai_settings, screen, ship):
        """Initialize instance of Bullet."""
        super(Bullet, self).__init__()
        self.screen = screen
        # NOTE: `.Rect` creates a Rect object, vs. line 24
        self.rect = pygame.Rect(0, 0, 15, 3)  # Origin coords, width, height of bullet
        self.rect.centerx = ship.rect.centerx  # Fire from center of the image
        # TODO: if changed to certain rect attr, get error 'invalid rect attribute'; can we change to a better message?
        self.rect.top = ship.rect.centery  # Align bullet to center of image
        self.x = float(self.rect.x)   # Declare x attribute
        self.color = (0, 0, 0)  # Black
        self.speed_factor = 1  # In px

    def update(self):
        """Move bullet across the screen."""
        self.x += self.speed_factor
        self.rect.x = self.x

    def draw_bullet(self):
        """Draw the bullet."""
        # NOTE: `.rect` is a method that draws a rect on a Surface
        pygame.draw.rect(self.screen, self.color, self.rect)
