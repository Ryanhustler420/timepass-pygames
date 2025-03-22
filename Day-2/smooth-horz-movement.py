import pygame
import math

pygame.init()

WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

x, y = WIDTH // 2, HEIGHT // 2
speed = 2
angle = 0  # Start with an initial angle
radius = 150  # Radius of the circular path

running = True
while running:
    screen.fill((0, 0, 0))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        angle -= 0.05  # Move left, decrease angle
    if keys[pygame.K_RIGHT]:
        angle += 0.05  # Move right, increase angle

    # Calculate new position using cosine for x-coordinate and sine for y-coordinate
    x = WIDTH // 2 + radius * math.cos(angle)  # Cosine for horizontal movement
    y = HEIGHT // 2 # + radius * math.sin(angle)  # Sine for vertical movement

    pygame.draw.circle(screen, (0, 255, 0), (int(x), int(y)), 10)

    for event in pygame.event.get():
        if event == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(60)  # FPS

pygame.quit()
