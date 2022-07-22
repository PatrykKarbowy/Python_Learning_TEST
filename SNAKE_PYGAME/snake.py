import pygame
from tkinter import messagebox
from random import randrange

WIDTH = 840
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("SNAKE")

# COLORS

RED = (255,0,0)
BLACK = (0,0,0)
WHITE = (255,255,255)
ORANGE = (255,165,0)

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    pass
                            
                    
        pygame.display.update()

main()