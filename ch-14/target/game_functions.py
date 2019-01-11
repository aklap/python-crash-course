import sys
from time import sleep
import pygame
from bullet import Bullet


def check_events(ai_settings, screen, ship, bullets, stats, play_button):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():  # NOTE: Our event loop, watch key events.
        if event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets, stats)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, play_button, ship, bullets, mouse_x, mouse_y)


def start_game(ai_settings, screen, ship, bullets, stats):
    """Start game."""
    # Hide mouse cursor when game starts
    pygame.mouse.set_visible(False)

    # Reset game stats
    stats.reset_stats()
    stats.game_active = True

    # Empty list of  and bullets
    bullets.empty()


def check_play_button(ai_settings, screen, stats, play_button, ship, bullets, mouse_x, mouse_y):
    """Start a new game when the player clicks Play."""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)

    if button_clicked and not stats.game_active:
        start_game(ai_settings, screen, ship, bullets, stats)


def check_keydown_events(event, ai_settings, screen, ship, bullets, stats):
    """Respond to keypresses."""
    if event.key == pygame.K_q:
        # NOTE: Exit the running process for our game, ie quit the game.
        sys.exit()
    elif event.key == pygame.K_p:
        # start game on key press of p
        start_game(ai_settings, screen, ship, bullets, stats)
    elif event.key == pygame.K_DOWN:
        # Move the ship rect to the down.
        ship.moving_down = True
    elif event.key == pygame.K_UP:
        # Move the ship rect to the up.
        ship.moving_up = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)


def check_keyup_events(event, ship):
    """Respond to key releases."""
    if event.key == pygame.K_DOWN:
        ship.moving_down = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False


def fire_bullet(ai_settings, screen, ship, bullets):
    """Fire bullet if limit not reached yet."""
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def update_bullets(ai_settings, screen, ship, bullets, target, stats):
    """Update position of bullets and get rid of old bullets."""
    check_bullet_target_collisions(ai_settings, screen, target, bullets, stats, ship)

    bullets.update()  # Change position of existing bullets

    for bullet in bullets.copy():  # Remove old bullets
        if bullet.rect.right >= screen.get_rect().right:
            bullets.remove(bullet)


def update_target(ai_settings, screen, target, bullets):
    """Check if a bullet has collided with a target and if so remove bullet-target."""
    if target.check_edges():
        target.change_direction()


def check_bullet_target_collisions(ai_settings, screen, target, bullets, stats, ship):

    if pygame.sprite.spritecollideany(target, bullets):
        # Destroy existing bullets, create new fleet.
        bullets.empty()
        target_hit(ai_settings, stats, screen, bullets, ship, target)
        ship.center_ship()

def target_hit(ai_settings, stats, screen, bullets, ship, target):
    stats.targets_left -= 1

    if stats.targets_left < 1:
        stats.game_active = False
        pygame.mouse.set_visible(True)
        print('game over')
    else:
        bullets.empty()
        ship.center_ship()
        sleep(0.5)


def update_screen(ai_settings, screen, ship, bullets, stats, play_button, target):
    # Redraw screen each pass of the loop and fill bg.
    screen.fill(ai_settings.bg_color)
    # Draw target:
    target.draw_target()
    # Draw each bullet in bullets set
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # Draw ship
    ship.blitme()
    # Draw play button only if game hasn't started
    if not stats.game_active:
        play_button.draw_button()
    # Make the most recently drawn screen visible.
    pygame.display.flip()

def reload_bullets(ai_settings, stats, screen, ship, bullets):
    """Reload bullets."""
    bullets.empty()
