import tkinter as tk
import numpy as np
from tkinter import Canvas

#GLOBAL CONSTANT
node_width = node_height = 30
start_x = start_y = 10

class Node():
    def __init__ (self, parent = None, position = None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__ (self, other):
        return self.position == other.position

class CanvasEvents(tk.Tk, Node):
    def __init__ (self, node = "node"):
        super().__init__()
        super(tk.Tk, self).__init__(node)

        self.title("A* PATHFINDING ALGORITM")
        self.canvas = Canvas(self)
        self.canvas.pack(expand = 1, fill = tk.BOTH)
        self.started = False

    def create_grid(self, rows, columns):
        for i in range(1,(rows+1)):
            for j in range(1,(columns+1)):
                node_rect = self.canvas.create_rectangle(
                start_x +(node_width * (j-1)), 
                start_y + (node_height * (i-1)), 
                ((start_x +(node_width * (j-1))) + node_width), 
                (start_y + (node_height * (i-1)) + node_height), 
                width=1, fill="white",
                tags = [i-1, j-1]
                )
        self.canvas.pack()
    def node_click_event_start(self, event):
            node = self.canvas.find_closest(event.x, event.y)
            self.canvas.itemconfigure(node, fill = "green")
            print(self.canvas.gettags("current")[0], self.canvas.gettags("current")[1])
            self.started = True
            print(self.started)
    def node_click_event_end(self, event):
            node = self.canvas.find_closest(event.x, event.y)
            self.canvas.itemconfigure(node, fill = "red")
            print(self.canvas.gettags("current")[0], self.canvas.gettags("current")[1])
    def node_click_event_barrier(self, event):
            node = self.canvas.find_closest(event.x, event.y)
            self.canvas.itemconfigure(node, fill = "black")
            print(self.canvas.gettags("current")[0], self.canvas.gettags("current")[1])

    
if __name__ == "__main__":
    node_grid = CanvasEvents()
    node_grid.create_grid(5,5)
    if node_grid.started == False:
        node_grid.canvas.tag_bind("current", '<Button-1>', node_grid.node_click_event_start)
    node_grid.canvas.tag_bind("current", "<Button-2>", node_grid.node_click_event_end)
    node_grid.canvas.tag_bind("current", "<Button-3>", node_grid.node_click_event_barrier)
    node_grid.mainloop()

