import pygame
import random

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
BALL_SIZE = 10
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PADDLE_SPEED = 5
AI_SPEED = 4  # AI Paddle Speed
BALL_SPEED_X = 5
BALL_SPEED_Y = 5
BALL_ACCELERATION = 1.05
WINNING_SCORE = 10

# Load sounds
# paddle_sound = pygame.mixer.Sound("paddle_hit.wav")
# wall_sound = pygame.mixer.Sound("wall_hit.wav")
# score_sound = pygame.mixer.Sound("score.wav")

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong with AI")

# Font setup
font = pygame.font.Font(None, 50)

# Function to display text
def draw_text(text, size, x, y):
    font_obj = pygame.font.Font(None, size)
    text_surface = font_obj.render(text, True, WHITE)
    screen.blit(text_surface, (x, y))

# Function to show the start screen
def show_start_screen():
    screen.fill(BLACK)
    draw_text("PING PONG - AI Mode", 50, WIDTH // 2 - 200, HEIGHT // 3)
    draw_text("Press SPACE to Start", 40, WIDTH // 2 - 150, HEIGHT // 2)
    pygame.display.flip()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                waiting = False

# Function to show the game over screen
def show_game_over(winner):
    screen.fill(BLACK)
    draw_text(f"{winner} WINS!", 50, WIDTH // 2 - 100, HEIGHT // 3)
    draw_text("Press SPACE to Restart", 40, WIDTH // 2 - 170, HEIGHT // 2)
    pygame.display.flip()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                waiting = False

# Main game function
def main():
    global BALL_SPEED_X, BALL_SPEED_Y
    
    # AI Paddle (Left)
    left_paddle = pygame.Rect(20, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
    # Player Paddle (Right)
    right_paddle = pygame.Rect(WIDTH - 30, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
    # Ball
    ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)
    # Scores
    left_score = 0
    right_score = 0

    show_start_screen()  # Show start screen before the game begins

    running = True
    while running:
        pygame.time.delay(10)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        # Player Controls
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and right_paddle.top > 0:
            right_paddle.y -= PADDLE_SPEED
        if keys[pygame.K_DOWN] and right_paddle.bottom < HEIGHT:
            right_paddle.y += PADDLE_SPEED

        # AI Movement - follows the ball
        if left_paddle.centery < ball.centery:
            left_paddle.y += AI_SPEED  # Move AI down
        elif left_paddle.centery > ball.centery:
            left_paddle.y -= AI_SPEED  # Move AI up

        # Ensure AI paddle stays within screen bounds
        left_paddle.y = max(0, min(left_paddle.y, HEIGHT - PADDLE_HEIGHT))

        # Move the ball
        ball.x += BALL_SPEED_X
        ball.y += BALL_SPEED_Y

        # Ball collision with top and bottom walls
        if ball.top <= 0 or ball.bottom >= HEIGHT:
            BALL_SPEED_Y = -BALL_SPEED_Y
            # wall_sound.play()

        # Ball collision with paddles
        if ball.colliderect(left_paddle):
            BALL_SPEED_X = abs(BALL_SPEED_X) * BALL_ACCELERATION
            hit_pos = (ball.centery - left_paddle.centery) / (PADDLE_HEIGHT / 2)
            BALL_SPEED_Y = hit_pos * 5
            # paddle_sound.play()

        if ball.colliderect(right_paddle):
            BALL_SPEED_X = -abs(BALL_SPEED_X) * BALL_ACCELERATION
            hit_pos = (ball.centery - right_paddle.centery) / (PADDLE_HEIGHT / 2)
            BALL_SPEED_Y = hit_pos * 5
            # paddle_sound.play()

        # Scoring system
        if ball.left <= 0:  # Player scores
            right_score += 1
            ball.x, ball.y = WIDTH // 2, HEIGHT // 2
            BALL_SPEED_X = random.choice([-5, 5])
            BALL_SPEED_Y = random.choice([-5, 5])
            # score_sound.play()

        if ball.right >= WIDTH:  # AI scores
            left_score += 1
            ball.x, ball.y = WIDTH // 2, HEIGHT // 2
            BALL_SPEED_X = random.choice([-5, 5])
            BALL_SPEED_Y = random.choice([-5, 5])
            # score_sound.play()

        # Check for game over
        if left_score >= WINNING_SCORE:
            show_game_over("AI")
            return main()  # Restart game
        if right_score >= WINNING_SCORE:
            show_game_over("Player")
            return main()  # Restart game

        # Drawing
        screen.fill(BLACK)
        pygame.draw.rect(screen, WHITE, left_paddle)
        pygame.draw.rect(screen, WHITE, right_paddle)
        pygame.draw.ellipse(screen, WHITE, ball)

        # Draw scores
        left_text = font.render(str(left_score), True, WHITE)
        right_text = font.render(str(right_score), True, WHITE)
        screen.blit(left_text, (WIDTH // 4, 20))
        screen.blit(right_text, (WIDTH * 3 // 4, 20))

        pygame.display.flip()  # Update display

# Start the game
main()
