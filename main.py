import pygame
import sys
import time

# Initialize Pygame
pygame.init()
start_time = time.time()
max_time = 50  # seconds

# Constants
WIDTH, HEIGHT = 600, 600
ROWS, COLS = 20, 20
TILE_SIZE = WIDTH // COLS

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
WALL = (30, 30, 30)
PLAYER = (255, 0, 0)
GOAL = (0, 255, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🏁 Escape the Maze")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 30)

# Maze map
maze = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1],
    [1,0,1,0,1,0,1,1,0,1,0,1,1,0,1,0,1,1,0,1],
    [1,0,1,0,0,0,0,1,0,1,0,0,1,0,0,0,1,0,0,1],
    [1,0,1,1,1,1,0,1,1,1,1,0,1,1,1,1,1,0,1,1],
    [1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,1,0,0,1],
    [1,1,1,1,0,1,1,1,1,0,1,1,1,1,1,0,1,1,0,1],
    [1,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,1,0,1],
    [1,0,1,1,1,1,1,0,1,1,1,1,1,0,1,1,0,1,0,1],
    [1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,1,0,1,0,1],
    [1,1,1,1,1,0,1,1,1,1,1,0,1,1,0,1,0,1,1,1],
    [1,0,0,0,1,0,0,0,0,0,1,0,0,1,0,0,0,0,0,1],
    [1,0,1,0,1,1,1,1,1,0,1,1,0,1,1,1,1,1,0,1],
    [1,0,1,0,0,0,0,0,1,0,0,1,0,0,0,0,0,1,0,1],
    [1,0,1,1,1,1,1,0,1,1,0,1,1,1,1,1,0,1,0,1],
    [1,0,0,0,0,0,1,0,0,1,0,0,0,0,0,1,0,0,0,1],
    [1,1,1,1,1,0,1,1,0,1,1,1,1,1,0,1,1,1,1,1],
    [1,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1],
    [1,0,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,'G',1],
]

# Start & goal positions
start_pos = [1, 1]
goal_pos = None
for y, row in enumerate(maze):
    for x, cell in enumerate(row):
        if cell == 'G':
            goal_pos = (x, y)
            maze[y][x] = 0

player_rect = pygame.Rect(start_pos[0]*TILE_SIZE, start_pos[1]*TILE_SIZE, TILE_SIZE, TILE_SIZE)

# Functions
screen.fill((30, 30, 30))
def draw_maze():
    screen.fill((50, 50, 50))  # Fill background grey (for debug)
    for y in range(ROWS):
        for x in range(COLS):
            rect = pygame.Rect(x*TILE_SIZE, y*TILE_SIZE, TILE_SIZE, TILE_SIZE)
            if (x, y) == goal_pos:
                pygame.draw.rect(screen, GOAL, rect)
            elif maze[y][x] == 1:
                pygame.draw.rect(screen, WALL, rect)
            else:
                pygame.draw.rect(screen, WHITE, rect)

def can_move(new_x, new_y):
    grid_x = new_x // TILE_SIZE
    grid_y = new_y // TILE_SIZE
    return maze[grid_y][grid_x] == 0 or (grid_x, grid_y) == goal_pos

def show_message(msg, color):
    text = font.render(msg, True, color)
    screen.blit(text, (WIDTH//2 - text.get_width()//2, HEIGHT//2 - text.get_height()//2))
    pygame.display.update()
    pygame.time.delay(3000)

# Main loop
running = True
while running:
    elapsed_time = int(time.time() - start_time)
    remaining_time = max_time - elapsed_time

    screen.fill(BLACK)
    draw_maze()
    pygame.draw.rect(screen, PLAYER, player_rect)

    # Show timer
    timer_text = font.render(f"⏱ Time Left: {remaining_time}s", True, WHITE)
    screen.blit(timer_text, (20, 20))

    if remaining_time <= 0:
        show_message("⛔ Time's Up! Game Over!", RED)
        break

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()
    new_x, new_y = player_rect.x, player_rect.y
    if keys[pygame.K_LEFT]:
        new_x -= TILE_SIZE
    if keys[pygame.K_RIGHT]:
        new_x += TILE_SIZE
    if keys[pygame.K_UP]:
        new_y -= TILE_SIZE
    if keys[pygame.K_DOWN]:
        new_y += TILE_SIZE

    if can_move(new_x, new_y):
        player_rect.x, player_rect.y = new_x, new_y

    if (player_rect.x // TILE_SIZE, player_rect.y // TILE_SIZE) == goal_pos:
        show_message("🎉 You Escaped!", YELLOW)
        break

    pygame.display.update()
    clock.tick(10)

pygame.quit()
sys.exit()
