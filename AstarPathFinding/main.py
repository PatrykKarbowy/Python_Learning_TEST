from node import Node
import numpy as np

def return_path(current_node, maze):
    path = []
    current = current_node
    rows_number, collumns_number = np.shape(maze)
    result = [[0 for i in range(rows_number + 1)] for j in range(collumns_number - 1)]
    while current is not None:
        path.append(current.position)
        current = current.parent

    path = path[::-1]
        
    for i in range(len(path)):
        result[path[i][0]][path[i][1]] = "#"
    
    return result

def search(maze, start, end):

    #Start conditions
    start_node = Node(None, tuple(start))
    start_node.g = start_node.h = start_node.f
    end_node = Node(None, tuple(end))
    end_node.g = end_node.h = end_node.f

    #Initating open and closing arrays
    open_nodes = []
    closed_nodes = []

    #Adding start node to the open points to start searching the final path
    open_nodes.append(start_node)

    #Creating iterator, to prevent program from crashing
    iterations = 0
    max_iterations = (len(maze) // 2) * 10

    #Allowed moves in 2D array
    move = [[-1, 0],    #up
            [0, 1],      #right
            [0, -1],     #left
            [1, 0]]     #down

    #Loop untill you find the end
    while len(open_nodes) > 0:
        iterations += 1

        current_node = open_nodes[0]
        current_index = 0
        for index, point in enumerate(open_nodes):
            if point.f < current_node.f:
                current_node = point
                current_index  = index
        
        if iterations > max_iterations:
            print("Too many iterations, failed to find the maze")
            return return_path(current_node, maze)
    
        open_nodes.pop(current_index)
        closed_nodes.append(current_node)

        if current_node == end_node:
            return return_path(current_node, maze)

        children = []

        rows_number, collumns_number = np.shape(maze)


        for new_position in move:

            new_node_position = (current_node.position[0] + new_position[0],
                            current_node.position[1] + new_position[1])

            if (new_node_position[0] > (rows_number - 1) or
                new_node_position[0] < 0 or
                new_node_position[1] > (collumns_number - 1) or
                new_node_position[1] < 0):
                continue

            if maze[new_node_position[0]][new_node_position[1]] != 0:
                continue

            new_node = Node(current_node, new_node_position)
            
            children.append(new_node)
        
        for child in children:
            
            if len([visited_child for visited_child in closed_nodes if visited_child == child]) > 0:
                continue

            child.g = current_node.g
            child.h = ((child.position[0] - end_node.position[0] ** 2) +
                        (child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            if len([visited_child for visited_child in open_nodes if visited_child == child and child.g > visited_child.g]) > 0:
                continue

            open_nodes.append(child)

if __name__ == '__main__':
    #MAZE
    maze = [[0,1,0,0,0,0],
            [0,1,0,0,1,0],
            [0,0,0,0,1,0],
            [0,0,1,0,0,0],
            [0,0,0,0,0,0]]

    start = [3,0]   #Start position
    end = [4,1]     #End position

    path = search(maze, start, end)     #Starting A* Pathfinding Algorithm

    #Block of code that formats path into string that visualizate it properly
    path_string = ""
    for index in path:
        for inside_index, path_symbol in enumerate(index):
            if inside_index < (len(index) - 1):
                path_string += str(path_symbol) + " "
            else:
                path_string += "\n"

    print(path_string)