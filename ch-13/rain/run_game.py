import pygame
import sys
from pygame.sprite import Sprite, Group

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

    def blitme(self):
        self.screen.blitme(self.image, self.rect)

    def update(self):
        """Move alien down the screen."""
        self.x += 1 # speed factor
        # self.rect.y = self.y

def run_game():
    """Run raindrop game."""
    # Initialize game
    pygame.init()
    # Create window
    screen = pygame.display.set_mode((1200, 800))
    # Add caption to window
    pygame.display.set_caption('Raindrop Game')
    # Create collection of Drop sprites
    drops = Group()
    # Create a single drop
    drop = Drop(screen)
    drop_width = drop.rect.width
    drop_height = drop.rect.height
    # drops.add(drop)
    # Available room for drops width wise
    available_space_x = 1200 - (drop_width * 2)
    # How many stars can fit width-wise on screen
    number_drops = int(available_space_x / (2 * drop_width))
    # Available space for rows of stars
    available_space_y = (800 - drop_height)
    number_rows = int(available_space_y / (2 * drop_height))

    # Create 'drop fleet': Generate total number of raindrops and store in Group()
    for row in range(number_rows):
        for drop_num in range(number_drops):
            # Create new instance of Drop
            drop = Drop(screen)
            drop_width = drop.rect.width
            drop.x = drop_width + (2 * drop_width * drop_num)
            drop.rect.x = drop.x
            drop.rect.y = drop.rect.height + (2 * drop.rect.height * row)
            drops.add(drop)

# Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()

        # Update rain drops position
        for drop in drops.sprites():

            drop.rect.y += 5

            # If drop is below bottom of screen, remove it and don't update it.
            if drop.rect.bottom >= screen.get_rect().height:
                drop.rect.y = 0

        # Update screen
        screen.fill((0, 0, 0))
        drops.draw(screen)
        pygame.display.flip()

run_game()