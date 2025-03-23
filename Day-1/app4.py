import pygame
import math
import random as r

pygame.init()

WIDTH, HEIGHT = 800, 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

CENTER_X, CENTER_Y = WIDTH // 2, HEIGHT // 2
RADIUS = 200

points = []

running = True
while running:
    screen.fill((0, 0, 0))
    
    mouse_x, mouse_y = pygame.mouse.get_pos()
    
    angle = math.atan2(mouse_y - CENTER_Y, mouse_x - CENTER_X)

    x = CENTER_X + RADIUS * math.cos(angle)
    y = CENTER_Y + RADIUS * math.sin(angle)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONUP:
            points.append({ "angle": angle, "x": x, "y": y })
            
    for _p in points:
        pygame.draw.circle(screen, (r.random() * 255, r.random() * 255, r.random() * 255), (int(_p['x']), int(_p['y'])), 5, 2)
        t_x = int(_p['x']) + RADIUS * math.cos(_p["angle"])
        t_y = int(_p['y']) + RADIUS * math.sin(_p["angle"])
        pygame.draw.line(screen, (0, 255, 0), (int(_p['x']), int(_p['y'])), (int(t_x), int(t_y)), 5)
    
    pygame.draw.circle(screen, (r.random() * 255, r.random() * 255, r.random() * 255), (int(x), int(y)), 5, 2)

    pygame.display.flip()
    clock.tick(300) # 60 FPS
            
pygame.quit()