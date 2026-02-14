import pygame
import random

# Initialize Pygame
pygame.init()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
BLUE = (50, 153, 213)

# Screen size
WIDTH = 1200
HEIGHT = 800

# Display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Feeding Game")

# Clock
clock = pygame.time.Clock()

# Snake settings
snake_block = 20
snake_speed = 15

# Load images (must be in same folder)
snake_image = pygame.image.load("snake.png").convert_alpha()
chicken_image = pygame.image.load("chicken.webp").convert_alpha()

snake_image = pygame.transform.scale(snake_image, (snake_block, snake_block))
chicken_image = pygame.transform.scale(chicken_image, (snake_block, snake_block))

# Fonts
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 30)


def draw_snake(snake_list):
    for x, y in snake_list:
        screen.blit(snake_image, (x, y))


def show_message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, (WIDTH // 6, HEIGHT // 3))


def show_score(score):
    value = score_font.render(f"Score: {score}", True, BLACK)
    screen.blit(value, (10, 10))


def gameLoop():
    game_over = False
    game_close = False

    x1 = WIDTH // 2
    y1 = HEIGHT // 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    snake_length = 1
    score = 0

    foodx = random.randrange(0, WIDTH - snake_block, snake_block)
    foody = random.randrange(0, HEIGHT - snake_block, snake_block)

    while not game_over:

        while game_close:
            screen.fill(BLUE)
            show_message("You Lost! Press C-Play Again or Q-Quit", RED)
            show_score(score)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False

                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        # Wall collision
        if x1 < 0 or x1 >= WIDTH or y1 < 0 or y1 >= HEIGHT:
            game_close = True

        x1 += x1_change
        y1 += y1_change

        screen.fill(BLUE)
        screen.blit(chicken_image, (foodx, foody))

        snake_head = [x1, y1]
        snake_list.append(snake_head)

        if len(snake_list) > snake_length:
            del snake_list[0]

        # Self collision
        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        draw_snake(snake_list)
        show_score(score)
        pygame.display.update()

        # Food collision
        if x1 == foodx and y1 == foody:
            foodx = random.randrange(0, WIDTH - snake_block, snake_block)
            foody = random.randrange(0, HEIGHT - snake_block, snake_block)
            snake_length += 1
            score += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()


# START GAME
gameLoop()
