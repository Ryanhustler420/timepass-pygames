import pygame
import math

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

bullets = []
gravity = .2

# Player (Gun) Position
gun_x, gun_y = 100, HEIGHT - 100  # Start from bottom left

running = True
while running:
    screen.fill((0, 0, 0))

    # Draw gun (just a simple circle)
    pygame.draw.circle(screen, (0, 255, 0), (gun_x, gun_y), 10)  # Green Gun

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            angle = math.atan2(my - HEIGHT, mx) # calculate angle
            speed = 10
            bullets.append({ 
                "x": gun_x, 
                "y": gun_y, 
                "vx": speed * math.cos(angle), 
                "vy": -speed * math.sin(angle), 
                "time": 0
            })

    for bullet in bullets:
        bullet["time"] += .1
        bullet["x"] += bullet["vx"]
        bullet["y"] += bullet["vy"] + (gravity * bullet["time"])

        pygame.draw.circle(screen, (255, 0, 0), (int(bullet["x"]), int(bullet["y"])), 5)

    pygame.display.flip()
    clock.tick(60)  # FPS

pygame.quit()
