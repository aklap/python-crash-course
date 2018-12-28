import sys
import pygame
from settings import Settings

class Rocket():
    """Base rocket class."""
    def __init__(self, settings, screen):
        """Initialize rocket."""
        self.screen = screen
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """Draw rocket at current location."""
        self.screen.blit(self.image, self.rect)


def run_game():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption('Rocket Game')
    bg_color = (0, 0, 0)
    rocket = Rocket(settings, screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(settings.bg_color)
        rocket.blitme()
        pygame.display.flip()

run_game()