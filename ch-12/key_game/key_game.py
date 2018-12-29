import pygame
import sys

# Initialize a pygame instance.
def run_game():
    pygame.init()
    # Settings
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption('Key Game')
    bg_color = (230, 230, 230)
    screen.fill(bg_color)
    font = pygame.font.SysFont('Arial', 65, True)
    screen_rect = screen.get_rect()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                # Get key as an integer, pass to key.name() to return human readable name
                key_name = pygame.key.name(event.key)
                text_surface = font.render(key_name, True, (0, 0, 0), bg_color)

                screen.fill(bg_color)  # Fill the window with a bg color
                screen.blit(text_surface, (screen_rect.centerx, screen_rect.centery))  # Draw text on window (text surface on window surface)
                pygame.display.flip()  # Draw the latest window

run_game()
