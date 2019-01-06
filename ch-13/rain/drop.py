import pygame
from pygame.sprite import Sprite


class Drop(Sprite):
    """Class to model a raindrop."""

    def __init__(self, screen):
        """Initialize an instance of Drop."""
        super(Drop, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/drop.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # Position drop
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.speed_factor = 1


def update(self):
    """Move alien down the screen."""
    self.x += self.speed_factor
