import sys
import pygame
from pygame.sprite import Sprite, Group


class Star(Sprite):
    """Base class Star."""

    def __init__(self, screen):
        """Initialize instance of Star."""
        super(Star, self).__init__()
        self.screen = screen
        # Load the star image
        self.image = pygame.image.load('images/star.png')
        self.rect = self.image.get_rect()
        # Position the star
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)


    def blitme(self):
        """Draw star at current position."""
        self.screen.blit(self.image, self.rect)


def run_game():
    """Initialize game, create window."""
    pygame.init()  # Initialize game
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption('Alien Invasion')
    # Stars
    star = Star(screen)
    star_width = star.rect.width
    star_height = star.rect.height
    stars = Group()

    # Available room for stars
    available_space_x = 1200 - (star_width * 2)
    # How many stars can fit width-wise on screen
    number_stars = int(available_space_x / (2 * star_width))
    # Available space for rows of stars
    available_space_y = (800 - (2 * star_height))
    number_rows = int(available_space_y / (2 * star_height))

    for row in range(number_rows):
        for star_num in range(number_stars):
            # Create new instance of Star
            star = Star(screen)
            star_width = star.rect.width
            star.x = star_width + 2 * star_width * star_num
            star.rect.x = star.x
            star.rect.y = star.rect.height + 2 * star.rect.height * row
            # Add new star to group
            stars.add(star)

    # Run game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()
            else:
                # Draw stars
                stars.draw(screen)
                # Re-render screen
                pygame.display.flip()

run_game()