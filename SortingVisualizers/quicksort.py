import pygame
from random import randrange

#WINDOWS SETUP
WIDTH = 800
HEIGHT = 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bubble sort Visualizer")

# DATA PROPERTIES
DATA_WIDTH = 2
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
        pygame.draw.line(WIN, WHITE, (col * DATA_WIDTH,HEIGHT), (col*DATA_WIDTH, generated_numbers[col]))
    clock = pygame.time.Clock()
    clock.tick(300)
    pygame.display.update()
        
def swap(i, j):
    generated_numbers[i], generated_numbers[j] = generated_numbers[j], generated_numbers[i]
    return generated_numbers

def quick_sort(array, left_edge, right_edge):
    if left_edge < right_edge:
        piv = partition(array, left_edge, right_edge)
        quick_sort(array, left_edge, piv - 1)
        quick_sort(array, piv + 1, right_edge)

def partition(array, left_edge, right_edge):
    pivot = array[right_edge]
    pointer = left_edge - 1
    for i in range(left_edge,right_edge):
        if array[i] < pivot:
            pointer += 1
            swap(pointer, i)
            draw_data()
    swap(pointer + 1, right_edge)
    return pointer + 1
                
#   MAIN GAME LOOP
def main():
    generate_data()
    quick_sort(generated_numbers, 0, len(generated_numbers) - 1)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
   
main()