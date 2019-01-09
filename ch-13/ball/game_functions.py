"""A module for game functions."""

import sys


import pygame
from ball import Ball
from person import Person
from random import randint


def update_screen(screen, ball, person):
    """Re-render screen."""
    screen.fill((230, 230, 230))
    ball.draw_ball()
    person.blitme(screen)
    pygame.display.flip()


def check_events(event, person):
    """Check and handle events."""
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            keydown_event(event, person)
        elif event.type == pygame.KEYUP:
            keyup_event(event, person)


def keydown_event(event, person):
    """Handle keydown events."""
    if event.key == pygame.K_q:
        sys.exit()
    elif event.key == pygame.K_RIGHT:
        # Move person to the right.
        person.moving_right = True
    elif event.key == pygame.K_LEFT:
        # Move person to the left.
        person.moving_left = True


def keyup_event(event, person):
    """Handle keydown events."""
    if event.key == pygame.K_RIGHT:
        person.moving_right = False
    elif event.key == pygame.K_LEFT:
        person.moving_left = False


def create_ball(screen):
    """Create an instance of Ball."""
    ball = Ball(10, 10, screen)
    position_ball(screen, ball)
    return ball


def position_ball(screen, ball):
    """Position ball instance on screen."""
    ball_width = ball.rect.width
    ball_height = ball.rect.height
    screen_rect = screen.get_rect()
    # Available width
    available_space_x = screen_rect.width - (ball_height * 2)
    # Position ball along top of screen
    ball.x = ball_width + (2 * ball_width + randint(0, available_space_x))
    ball.rect.x = ball.x
    ball.rect.y = ball.rect.height + (2 * ball.rect.height)


def create_person(screen):
    """Create an instance of Person."""
    return Person(screen)


def update_ball(ball, person):
    """Update the position of the ball instance."""
    check_collision(ball, person)
    check_bottom(ball)
    ball.update()


def update_person(person):
    """Update position of the person instance."""
    person.update()


def check_collision(ball, person):
    """Check if ball collides with person."""
    if pygame.sprite.collide_rect(ball, person):
        ball.y = 0  # send back to top of screen
        ball.rect.x = randint(0, 1200)  # change position along top of screen


def check_bottom(ball):
    """Check if ball is at bottom of window."""
    if ball.rect.bottom >= ball.screen_rect.height:
        ball.to_top()
