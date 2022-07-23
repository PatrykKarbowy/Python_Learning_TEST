import pygame
from tkinter import messagebox
from random import randrange

#WINDOWS SETUP
WIDTH = 900
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("SNAKE")

# COLORS
RED = (255,0,0)
BLACK = (0,0,0)
WHITE = (255,255,255)
ORANGE = (255,165,0)

# SNAKE SIZE
SIZE = 30

# GRID
ROWS = WIDTH // SIZE
COLUMNS = WIDTH // SIZE

class Snake():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.x_speed = 1
        self.y_speed = 0
        tail = []
        self.tail = tail

    def move(self):
        keys = pygame.key.get_pressed()
        if self.x_speed == 0:
            if keys[pygame.K_RIGHT]:
                self.x_speed = 1
                self.y_speed = 0
            if keys[pygame.K_LEFT]:
                self.x_speed = -1
                self.y_speed = 0
        elif self.y_speed == 0:
            if keys[pygame.K_UP]:
                self.x_speed = 0
                self.y_speed = -1
            if keys[pygame.K_DOWN]:
                self.x_speed = 0
                self.y_speed = 1

        self.tail.insert(0, Segment(self.x, self.y))
        self.x += self.x_speed
        self.y += self.y_speed

        if self.x < 0 or self.x == COLUMNS or self.y < 0 or self. y == ROWS:
            pygame.quit()

        if self.x == food.x and self.y == food.y:
            food.x = randrange(0,COLUMNS)
            food.y = randrange(0,ROWS)
        else:
            self.tail.pop()

    def draw(self):
        for segment in self.tail:
            segment.draw()
        pygame.draw.rect(WIN, ORANGE, (self.x * SIZE, self.y * SIZE, SIZE, SIZE))

class Segment():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def draw(self):
        pygame.draw.rect(WIN, WHITE, (self.x * SIZE, self.y * SIZE, SIZE, SIZE))

class Food():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def draw(self):
        pygame.draw.rect(WIN, RED, (self.x * SIZE, self.y * SIZE, SIZE, SIZE))

snake  = Snake(15,15)
food = Food(randrange(0,COLUMNS),randrange(0,ROWS))

def render_screen():
    WIN.fill(BLACK)
    snake.draw()
    food.draw()
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        snake.move()
        render_screen()                        
        clock.tick(10)

main()