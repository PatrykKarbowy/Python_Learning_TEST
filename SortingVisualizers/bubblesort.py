import pygame
from random import randrange

#WINDOWS SETUP
WIDTH = 800
HEIGHT = 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bubble sort Visualizer")

# DATA PROPERTIES
DATA_WIDTH = 10
COLUMNS = WIDTH // DATA_WIDTH

# COLORS
BLACK = (0,0,0)
WHITE = (255,255,255)

# Global arrays
generated_numbers = []

def generate_data():
    for col in range(COLUMNS):
        random_number = randrange(1, HEIGHT)
        generated_numbers.append(random_number)
        
def draw_data():
    WIN.fill(BLACK)
    for col in range(COLUMNS):
        pygame.draw.line(WIN, WHITE, (col * DATA_WIDTH,HEIGHT), (col*DATA_WIDTH, generated_numbers[col]),DATA_WIDTH // 2)
    clock = pygame.time.Clock()
    clock.tick(300)
    pygame.display.update()
        
def swap(i, j):
    generated_numbers[i], generated_numbers[j] = generated_numbers[j], generated_numbers[i]
    return generated_numbers

def bubble_sort():
    for i in range(len(generated_numbers) - 1):
        swapped = False
        for i in range(len(generated_numbers) - 1):
            if generated_numbers[i] > generated_numbers[i+1]:
                swap(i, (i+1))
                swapped = True
            draw_data()
        if not swapped:
            break
                
#   MAIN GAME LOOP
def main():
    generate_data()
    bubble_sort()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
   
main()