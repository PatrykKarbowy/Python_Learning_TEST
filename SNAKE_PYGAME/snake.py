import pygame
from random import randrange

#WINDOWS SETUP
WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("SNAKE")

# COLORS
RED = (255,0,0)
BLACK = (0,0,0)
DARK_GREY = (169,169,169)
ORANGE = (255,165,0)
GREY = (64,64,64)

# SNAKE SIZE
SIZE = 80

# GRID
ROWS = WIDTH // SIZE
COLUMNS = WIDTH // SIZE

# SNAKE CLASS
class Snake():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.x_speed = 1
        self.y_speed = 0
        tail = []
        self.tail = tail

    def move(self):

        # PERFORMING MOVE ACTIONS ACCORDING TO CLICKED BUTTON
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

        # MOVING SNAKE
        self.tail.insert(0, Segment(self.x, self.y))
        self.x += self.x_speed
        self.y += self.y_speed

        # CHECKING IF SNAKE IS INSIDE WINDOW
        if self.x < 0 or self.x == COLUMNS or self.y < 0 or self. y == ROWS:
            pygame.quit()

        # CHECKING IF SNAKE HEAD TOUCHED IT'S TAIL
        for segment in self.tail[1:]:
            if self.x == segment.x and self.y == segment.y:
                pygame.quit()

        # GENERATING NEW FOOD
        if self.x == food.x and self.y == food.y:
            while True:
                food.x = randrange(0,COLUMNS)
                food.y = randrange(0,ROWS)
                if len(list(filter(lambda segment: segment.x == food.x and segment.y == food.y, self.tail))) > 0:
                    continue
                else:
                    break
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
        pygame.draw.rect(WIN, DARK_GREY, (self.x * SIZE, self.y * SIZE, SIZE, SIZE))

class Food():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def draw(self):
        pygame.draw.rect(WIN, RED, (self.x * SIZE, self.y * SIZE, SIZE, SIZE))

# SETTING UP GAME OBJECTS
snake  = Snake(COLUMNS // 2, ROWS // 2)
food = Food(randrange(0,COLUMNS),randrange(0,ROWS))

# SCREEN RENDER
def render_screen():
    WIN.fill(BLACK)
    draw_grid()
    snake.draw()
    food.draw()
    pygame.display.update()

# FUNCTION THAT DRAWS GRID
def draw_grid():
    for row in range(ROWS):
        pygame.draw.line(WIN, GREY, (row*SIZE - 1, 0), (row*SIZE - 1, WIDTH), 2)
        pygame.draw.line(WIN, GREY, (0, row*SIZE - 1), (WIDTH, row*SIZE - 1), 2)

#   MAIN GAME LOOP
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