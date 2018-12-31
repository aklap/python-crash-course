import pygame

"""Base ship Class"""
class Ship():
    def __init__(self, settings, screen):
        """Initialize an instance of Ship."""
        self.screen = screen
        self.ai_settings = settings
        self.image = pygame.image.load('images/ship.bmp')
        # Turn image rect sideways
        self.image = pygame.transform.rotate(self.image,270)
        # Position ship in window
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # Position ship on leftmost side of window
        self.rect.left = self.screen_rect.left
        # Position ship in the center of the window
        self.rect.y = self.screen_rect.centery
        # Movement flags
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Prevent ship from moving out of window"""
        if self.moving_up and self.rect.y > self.screen_rect.top:
            self.rect.y -= self.ai_settings.ship_speed
        if self.moving_down and self.rect.y < self.screen_rect.bottom:
            self.rect.y += self.ai_settings.ship_speed
