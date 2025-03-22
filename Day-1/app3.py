import pygame
import math

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))

RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

center_x, center_y = width // 2, height // 2
radius = 200

clock = pygame.time.Clock()

def draw_arrow(surface, start_x, start_y, angle, length):
    # Arrow parameters
    arrow_size = 15
    
    # Arrow head (only to upper triangle part)
    end_x = start_x + length * math.cos(angle)
    end_y = start_y + length * math.sin(angle)

    # Draw the main line of the arrow
    pygame.draw.line(surface, RED, (start_x, start_y), (end_x, end_y), 5)

    # cos - x
    # sig - y
    # https://www.mathsisfun.com/algebra/trig-interactive-unit-circle.html

    # Draw the arrow head
    pygame.draw.polygon(surface, RED, [
        (end_x, end_y),
        (end_x - arrow_size * math.cos(angle - math.pi / 6), end_y - arrow_size * math.sin(angle - math.pi / 6)),
        (end_x - arrow_size * math.cos(angle + math.pi / 6), end_y - arrow_size * math.sin(angle + math.pi / 6))
    ])

arrows = []

# Main game loop
running = True
while running:
    screen.fill(BLACK)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Get mouse position
            mouse_x, mouse_y = pygame.mouse.get_pos()

            # Calculate the angle using atan2 (mouse position relative to the center)
            angle = math.atan2(mouse_y - center_y, mouse_x - center_x)

            arrows.append({ "center_x": center_x, "center_y": center_y, "angle": angle, "radius": radius })

    for arrow in arrows:
        # Draw the arrow pointing in the direction of the mouse click
        draw_arrow(screen, arrow["center_x"], arrow["center_y"], arrow["angle"], arrow["radius"])
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()


# --------------------------
# DRY RUN THIS CODE, TO UNDERSTAND ATAN2 AND POLYGON
# --------------------------