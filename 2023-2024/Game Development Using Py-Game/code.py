import pygame

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Brick Breaker")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

# Paddle properties
paddle_width = 100
paddle_height = 10
paddle_speed = 20

# Ball properties
ball_radius = 10
ball_speed_x = 5
ball_speed_y = 5

# Brick properties
brick_width = 100
brick_height = 20
bricks = []

# Create paddle
paddle = pygame.Rect(screen_width // 2 - paddle_width // 2, screen_height - 50, paddle_width, paddle_height)

# Create ball
ball = pygame.Rect(screen_width // 2 - ball_radius, screen_height // 2 - ball_radius, ball_radius * 2, ball_radius * 2)

# Create bricks
for i in range(8):
    for j in range(8):
        brick = pygame.Rect(j * (brick_width + 2) + 5, i * (brick_height + 2) + 5, brick_width, brick_height)
        bricks.append(brick)

# Ball movement
ball_dx = ball_speed_x
ball_dy = ball_speed_y

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move paddle
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.x -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle.right < screen_width:
        paddle.x += paddle_speed

    # Move ball
    ball.x += ball_dx
    ball.y += ball_dy

    # Ball collision with walls
    if ball.top <= 0:
        ball_dy *= -1
    if ball.left <= 0 or ball.right >= screen_width:
        ball_dx *= -1

    # Ball collision with paddle
    if ball.colliderect(paddle) and ball_dy > 0:
        ball_dy *= -1

    # Ball collision with bricks
    for brick in bricks:
        if ball.colliderect(brick):
            bricks.remove(brick)
            ball_dy *= -1

    # Draw everything
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, paddle)
    pygame.draw.ellipse(screen, RED, ball)
    for brick in bricks:
        pygame.draw.rect(screen, GREEN, brick)
    pygame.display.flip()

    # Check if all bricks are destroyed
    if len(bricks) == 0:
        running = False

    # Cap the frame rate
    pygame.time.Clock().tick(60)

pygame.quit()
