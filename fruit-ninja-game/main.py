import pygame
import random
import os
import sys

# Initialize pygame
pygame.init()

# Screen settings
WIDTH = 800
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fruit Ninja")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (50, 150, 255)

# Game variables
fruits = []
score = 0
level = 1
font = pygame.font.Font(None, 36)
GAME_DURATION = 60  # seconds
start_ticks = pygame.time.get_ticks()
clock = pygame.time.Clock()

# Load high score
HIGH_SCORE_FILE = "highscore.txt"
if os.path.exists(HIGH_SCORE_FILE):
    with open(HIGH_SCORE_FILE, "r") as f:
        high_score = int(f.read())
else:
    high_score = 0

# Load background (optional)
if os.path.exists("background.jpg"):
    background = pygame.image.load("background.jpg")
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
else:
    background = None

# Fruit class
class Fruit:
    def __init__(self, speed_boost=0):
        self.type = random.choice(["apple", "banana", "watermelon", "bomb"])
        self.x = random.randint(50, WIDTH - 50)
        self.y = HEIGHT
        self.speed = random.randint(5, 10 + speed_boost)

        img_file = f"{self.type}.png"
        if not os.path.exists(img_file):
            print(f"Missing image: {img_file}")
            sys.exit()

        self.image = pygame.image.load(img_file)
        self.image = pygame.transform.scale(self.image, (60, 60))

    def move(self):
        self.y -= self.speed

    def draw(self):
        screen.blit(self.image, (self.x, self.y))

# Game loop
running = True
while running:
    # Background
    if background:
        screen.blit(background, (0, 0))
    else:
        screen.fill(BLUE)

    # Timer
    seconds_passed = (pygame.time.get_ticks() - start_ticks) // 1000
    time_left = GAME_DURATION - seconds_passed
    if time_left <= 0:
        running = False

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            for fruit in fruits[:]:
                if fruit.x < mx < fruit.x + 60 and fruit.y < my < fruit.y + 60:
                    if fruit.type == "bomb":
                        running = False
                    else:
                        fruits.remove(fruit)
                        score += 1

    # Increase level based on score
    if score >= 20:
        level = 3
    elif score >= 10:
        level = 2

    # Add new fruit
    if random.randint(1, 30 - level * 5) == 1:
        fruits.append(Fruit(speed_boost=level * 2))

    # Update and draw fruits
    for fruit in fruits[:]:
        fruit.move()
        fruit.draw()
        if fruit.y + 60 < 0:
            fruits.remove(fruit)

    # Draw score and time
    score_text = font.render(f"Score: {score}", True, WHITE)
    level_text = font.render(f"Level: {level}", True, WHITE)
    timer_text = font.render(f"Time: {time_left}", True, WHITE)
    high_score_text = font.render(f"High Score: {high_score}", True, WHITE)

    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 50))
    screen.blit(timer_text, (WIDTH - 150, 10))
    screen.blit(high_score_text, (WIDTH - 220, 50))

    pygame.display.flip()
    clock.tick(30)

# Save high score
if score > high_score:
    with open(HIGH_SCORE_FILE, "w") as f:
        f.write(str(score))

pygame.quit()
sys.exit()
