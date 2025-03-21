import pygame
import sys

# Initialize pygame
pygame.init()

# Define window dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Click to Draw Line")
clock = pygame.time.Clock()

# Define colors
WHITE = (0, 0, 0)
RED = (255, 0, 0)

# Get the center of the window
center = (WIDTH // 2, HEIGHT // 2)

lines = []

# Main game loop
running = True
while running:
    screen.fill(WHITE)  # Fill the screen with white background
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Get the mouse position when clicked
            mouse_x, mouse_y = pygame.mouse.get_pos()

            lines.append({ "mouse_x": mouse_x, "mouse_y": mouse_y })

    for i in range(1, len(lines)):
        # we want to connect all the dots with the last ending
        pygame.draw.line(screen, RED, (lines[i-1]['mouse_x'], lines[i-1]['mouse_y']), (lines[i]['mouse_x'], lines[i]['mouse_y']), 2)
        pygame.draw.circle(screen, RED, (lines[i]['mouse_x'], lines[i]['mouse_y']), 5)

    # Update the display
    pygame.display.flip()
    clock.tick(60)

# Quit pygame
pygame.quit()
sys.exit()
