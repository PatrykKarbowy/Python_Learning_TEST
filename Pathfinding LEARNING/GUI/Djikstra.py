import pygame
from tkinter import messagebox
#WINDOW SETUP

WIDTH = 800
WIN = pygame.display.set_mode((WIDTH,WIDTH))
pygame.display.set_caption("Dijkstra Path Finding Algorithm")

# COLORS

RED = (255,0,0)
GREEN = (0,255,0)
BLACK = (0,0,0)
WHITE = (255,255,255)
ORANGE = (255,165,0)
BLUE = (0,0,200)
PURPLE = (150,0,210)

# BOX SETUP

columns = 40
rows = 40

box_height = WIDTH // rows
box_width = WIDTH // columns

# GLOBAL ARRAYS

grid = []
queue = []
path = []

class Node:
    def __init__ (self, col, row):
        self.x = col
        self.y = row
        self.start = False
        self.end = False
        self.wall = False
        self.queued = False
        self.visited = False
        self.neighbours = []
        self.prior = None

    def draw(self, win, color):
        pygame.draw.rect(win, color, (self.x * box_width, self.y * box_height, box_width - 1, box_height - 1))

    def set_neighbours(self):
        if self.x > 0:
            self.neighbours.append(grid[self.x - 1][self.y])
        if self.x < columns - 1:
            self.neighbours.append(grid[self.x + 1][self.y])
        if self.y > 0:
            self.neighbours.append(grid[self.x][self.y - 1])
        if self.y < rows - 1:
            self.neighbours.append(grid[self.x][self.y + 1])

    def reset(self):
        self.start = False
        self.end = False
        self.wall = False
        self.queued = False
        self.visited = False

def make_grid(cols, rows):
    for col in range(cols):
        arr = []
        for row in range(rows):
            arr.append(Node(col, row))
        grid.append(arr)

def draw_grid(win, color, cols, rows):
    for col in range(cols):
        for row in range(rows):
            node = grid[col][row]
            node.draw(win, color)

            if node.queued:
                node.draw(win, RED)
            if node.visited:
                node.draw(win, GREEN)
            if node in path:
                node.draw(win, BLUE)
            if node.start:
                node.draw(win, PURPLE)
            if node.end:
                node.draw(win, ORANGE)
            if node.wall:
                node.draw(win, BLACK)  
          
                
def set_neighbours(cols, rows):
    for col in range(cols):
        for row in range(rows):
            grid[col][row].set_neighbours()

def get_clicked_node(x, y):
    col = x // box_width
    row = y // box_height
    return grid[col][row]

def main():
    make_grid(columns, rows)
    set_neighbours(columns, rows)
    start_node_set = False
    end_node_set = False
    begin_search = False
    searching = True
    start_node = None
    end_node = None

    while True:
        for event in pygame.event.get():
            # Quit program
            if event.type == pygame.QUIT:
                pygame.quit()
            # Click handling - SET NODES
            if pygame.mouse.get_pressed()[0] and not start_node_set: # LEFT MOUSE BUTTON
                x, y = pygame.mouse.get_pos()
                start_node = get_clicked_node(x, y)
                start_node.start = True
                start_node_set = True
                start_node.visited = True
                start_node.touched = True
                queue.append(start_node)
            if pygame.mouse.get_pressed()[2] and not end_node_set: # RIGHT MOUSE BUTTON
                x, y = pygame.mouse.get_pos()
                end_node = get_clicked_node(x,y)
                if end_node.start:
                    break
                end_node.end = True
                end_node_set = True
                end_node.touched = True
            if pygame.mouse.get_pressed()[1] and not begin_search: # MOUSE WHEEL BUTTON
                x, y = pygame.mouse.get_pos()
                node = get_clicked_node(x, y)
                if node.start or node.end:
                    break
                node.wall = True
                node.touched = True


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and end_node_set:
                    begin_search = True
                if event.key == pygame.K_DELETE:
                        x,y = pygame.mouse.get_pos()
                        node = get_clicked_node(x,y)
                        if node.start:
                            node.reset()
                            start_node_set = False
                            queue.pop(0)
                        elif node.end:
                            node.reset()
                            end_node_set = False
                        elif node.wall:
                            node.reset()
                        node.draw(WIN,WHITE)
            
        if begin_search:
            if len(queue) > 0 and searching:
                current_node = queue.pop(0)
                current_node.visited = True
                if current_node == end_node:
                    searching = False
                    while current_node.prior != start_node:
                        path.append(current_node.prior)
                        current_node = current_node.prior
                else:
                    for neighbour in current_node.neighbours:
                        if not neighbour.queued and not neighbour.wall:
                            neighbour.queued = True
                            neighbour.prior = current_node
                            queue.append(neighbour)
            elif len(queue) == 0:
                messagebox.showinfo('NO WAY OUT ERROR','Unfortunatelly there is no way to connect those two points. Try Again!')
                pygame.quit()

        draw_grid(WIN, WHITE, columns, rows)
        pygame.display.update()
  

main()
