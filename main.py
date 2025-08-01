import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen size
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Game")

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill background with black
    screen.fill((0, 0, 0))

    # Example: draw a white rectangle (maze wall)
    pygame.draw.rect(screen, (255, 255, 255), (100, 100, 100, 100))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()