import pygame
import random

# إعدادات اللعبة
pygame.init()
WIDTH, HEIGHT = 600, 400
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game 🐍")

clock = pygame.time.Clock()
BLOCK = 20

# الألوان
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
BLACK = (0, 0, 0)

# الثعبان
snake = [(100, 100)]
direction = "RIGHT"

# الطعام
food = (
    random.randrange(0, WIDTH, BLOCK),
    random.randrange(0, HEIGHT, BLOCK)
)

score = 0
font = pygame.font.SysFont(None, 35)

def draw():
    win.fill(BLACK)
    for part in snake:
        pygame.draw.rect(win, GREEN, (*part, BLOCK, BLOCK))
    pygame.draw.rect(win, RED, (*food, BLOCK, BLOCK))

    text = font.render(f"Score: {score}", True, WHITE)
    win.blit(text, (10, 10))
    pygame.display.update()

running = True
while running:
    clock.tick(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != "DOWN":
                direction = "UP"
            if event.key == pygame.K_DOWN and direction != "UP":
                direction = "DOWN"
            if event.key == pygame.K_LEFT and direction != "RIGHT":
                direction = "LEFT"
            if event.key == pygame.K_RIGHT and direction != "LEFT":
                direction = "RIGHT"

    x, y = snake[0]
    if direction == "UP":
        y -= BLOCK
    if direction == "DOWN":
        y += BLOCK
    if direction == "LEFT":
        x -= BLOCK
    if direction == "RIGHT":
        x += BLOCK

    new_head = (x, y)

    # اصطدام
    if (
        x < 0 or x >= WIDTH or
        y < 0 or y >= HEIGHT or
        new_head in snake
    ):
        running = False

    snake.insert(0, new_head)

    if new_head == food:
        score += 1
        food = (
            random.randrange(0, WIDTH, BLOCK),
            random.randrange(0, HEIGHT, BLOCK)
        )
    else:
        snake.pop()

    draw()

pygame.quit()