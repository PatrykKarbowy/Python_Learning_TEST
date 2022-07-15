import node
import numpy as np

def return_path(current_node, maze):
    path = []
    current = current_node
    rows_number, collumns_number = np.shape(maze)
    result = [[0 for i in range(collumns_number)] for j in range(rows_number)]
    path = path[::-1]
    while current is not None:
        path.append(current)
        current = current.parent
    for i in range(len(path)):
        result[[path[i][0]], [path[i][1]]] = "#"
    
    return result

def search(maze, start, end):

    #Start conditions
    start_node = node(None, tuple(start))
    start_node.g = start_node.h = start_node.f
    end_node = node(None, tuple(end))
    end_node.g = end_node.h = end_node.f

    #Initating open and closing arrays
    open_points = []
    closed_points = []

    #Adding start node to the open points to start searching the final path
    open_points.append(start_node)

    #Creating iterator, to prevent program from crashing
    iterations = 0
    max_iterations = (len(maze) // 2) * 10

    #Allowed moves in 2D array
    move = [[-1, 0],    #up
            [0, 1]      #right
            [0, -1]     #left
            [1, 0]]     #down

    #Loop untill you find the end
    while len(open_points) > 0:
        iterations += 1

        current_node = open_points[0]
        current_index = 0
        for index, point in enumerate(open_points):
            if point.f < current_node.f:
                current_node = point
                current_index  = index
        
        if iterations > max_iterations:
            print("Too many iterations, failed to find the maze")
            return return_path(current_node, maze)
    
        open_points.pop(current_index)
        closed_points.append(current_node)

        if current_node == end_node:
            return return_path(current_node, maze)

        children = []

        for new_position in move:

            node_position = (current_node.position[0] + new_position.position[0],
                            current_node.position[1] + new_position[1])
            