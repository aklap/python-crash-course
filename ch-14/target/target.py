import pygame
from pygame.sprite import Sprite

class Target(Sprite):
    """Represent a shooting target."""


    def __init__(self, ai_settings, screen):
        """Initialize instance of Target."""
        super(Target, self).__init__()
        self.ai_settings = ai_settings
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.rect = pygame.Rect(0, 0, ai_settings.target_width, ai_settings.target_height)
        self.rect.centerx = self.screen_rect.top
        self.rect.top = self.screen_rect.top
        self.rect.right = self.screen_rect.right
        self.y = float(self.rect.y)
        self.color = (0, 0, 0)
        self.speed_factor = ai_settings.target_speed_factor
        # Direction flag, up or down 1 or -1
        self.direction = 1

    def change_direction(self):
        """Flip direction of instance."""
        self.direction *= -1

    def check_edges(self):
        """Check if a target has hit top or bottom of the screen, if so flip direction."""
        if self.rect.top <= self.screen_rect.top:
            return True
        if self.rect.bottom >= self.screen_rect.bottom:
            return True

    def update(self):
        """Move target up and down the screen."""
        self.y += self.speed_factor * self.direction
        self.rect.y = self.y

    def to_top(self):
        """Send target back to top of screen."""
        self.y = 0

    def draw_target(self):
        """Draw target."""
        pygame.draw.rect(self.screen, self.color, self.rect)

