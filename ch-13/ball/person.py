import pygame
from pygame.sprite import Sprite


class Person(Sprite):
    """A class to represent a person to catch a ball."""
    def __init__(self, screen):
        """Initialize instance of Person."""
        super(Person, self).__init__()
        self.screen = screen
        # Load image and set rect attr.
        self.image = pygame.image.load('images/person-pointing.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # Start each person near bottom middle of window
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)
        # Movement
        self.moving_right = False
        self.moving_left = False
        self.person_speed_factor = 5

    def update(self):
        """Move Person left and right across screen."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.person_speed_factor

        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.center -= self.person_speed_factor

        self.rect.centerx = self.center

    def blitme(self, screen):
        """Draw the person at current location"""
        self.screen.blit(self.image, self.rect)