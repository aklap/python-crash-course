import pygame
import sys
from pygame.sprite import Sprite, Group
from random import *


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

    def blitme(self, screen):
        """Draw the person at current location"""
        self.screen.blit(self.image, self.rect)


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
        self.y += 5
        self.rect.y = self.y


    def draw_ball(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)


def run_game():
    """Run game."""
    # Initialize game
    pygame.init()
    # Create window
    screen = pygame.display.set_mode((1200, 800))
    # Create caption
    pygame.display.set_caption('Catch Game')
    # Create balls Group to collect all balls
    balls = Group()
    # Generate a ball and add to Group
    ball = Ball(10, 10, screen)
    ball_width = ball.rect.width
    ball_height = ball.rect.height

    # Available width for balls to drop
    available_space_x = 1200 - (ball_height * 2)
    # How many balls can fit width-wise on screen
    # number_balls = int(available_space_x / (2 * ball_width))
    # Position ball along top of screen and add to Group
    ball.x = ball_width + (2 * ball_width * randint(1, 10))
    ball.rect.x = ball.x
    ball.rect.y = ball.rect.height + (2 * ball.rect.height)
    balls.add(ball)

    # Create a person
    catcher = Person(screen)

    # Run loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()

        # Update balls
        balls.update()

        # Update screen

        for ball in balls.sprites():
            print(ball.x, ball.y)
            # Remove a ball if it falls past the bottom of screen
            if ball.rect.bottom >= screen.get_rect().height:
                ball.y = 0  # send back to top of screen
                # NOTE: Why does it have to be `rect.x` instead of ball.x?
                ball.rect.x = randint(0, 1200)  # change position along top of screen

        screen.fill((230, 230, 230))
        ball.draw_ball()
        catcher.blitme(screen)
        pygame.display.flip()

run_game()