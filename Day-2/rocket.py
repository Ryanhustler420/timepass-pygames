import pygame
import math

pygame.init()

WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

x, y = WIDTH // 2, HEIGHT // 2 # starts in the middle
angle = 0 # facing right
speed = 3 # movement speed

# Game Loop (Business Logic)
running = True
while running:
    screen.fill((0, 0, 0))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]: # Rotate Left
        angle -= 2
    if keys[pygame.K_RIGHT]: # Rotate Right
        angle += 2
    if keys[pygame.K_UP]: # Move forward
        x += speed * math.cos(math.radians(angle))
        y += speed * math.sin(math.radians(angle))

    pygame.draw.circle(screen, (0, 255, 0), (int(x), int(y)), 10) # Green Dot

    for event in pygame.event.get():
        if event == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(60) # FPS