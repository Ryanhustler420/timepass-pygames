import pygame
import math

pygame.init()

WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Circle settings
cx, cy = WIDTH // 2, HEIGHT // 2 # center of the circle
radius = 100 # Radius of movement
angle = 0 # Initial Angle

running = True

while running:
    screen.fill((0, 0, 0))

    x = cx + radius * math.cos(math.radians(angle))
    y = cy + radius * math.sin(math.radians(angle))

    pygame.draw.circle(screen, (0, 255, 0), (int(x), int(y)), 2)

    if angle >= 360:
        angle = 0
    else:
        angle += 0.5

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(60) # FPS

pygame.quit()