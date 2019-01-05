import sys
import pygame
from pygame.sprite import Sprite, Group


class Raindrop(Sprite):
    """A class to represent raindrops."""
    def __init__(self, screen):
        super(Raindrop, self).__init__()
        self.screen = screen
        # Load image
        self.image = pygame.image.load('images/raindrop.png')
        # Position image in window
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)


def run_game():
    # Initialize game
    pygame.init()
    # Initialize screen
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption('Rain')
    drop = Raindrop(screen)
    raindrops = Group()
    raindrops.add(drop)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()
            else:
                # Draw drops
                raindrops.draw(screen)
                pygame.display.flip()

run_game()