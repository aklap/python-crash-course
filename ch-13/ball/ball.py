import pygame
from pygame.sprite import Sprite
from random import randint

class Ball(Sprite):
    """A class to manage balls being thrown."""

    def __init__(self, ball_height, ball_width, screen):
        """Create a ball object."""
        super(Ball, self).__init__()
        self.screen = screen
        # Create a rect for a ball
        self.rect = pygame.Rect(0, 0, ball_height, ball_width)
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.top
        self.rect.top = self.screen_rect.top
        self.y = float(self.rect.y)
        self.color = (0, 0, 0)
        self.speed = 1


    def update(self):
            """Move bullet down the screen."""
            self.y += 2
            self.rect.y = self.y


    def draw_ball(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)


    def to_top(self):
        """Send ball back to the top of the window."""
        # Send ball back to top of screen in a different x pos
        self.y = 0
        # NOTE: Why does it have to be `rect.x` instead of self.x?
        self.rect.x = randint(0, 1200)  # change position along top of screen