import Node

def astar(maze, start, end):

    start_node = Node(None, start)
    start_node.g = start.node.h = start.node.f = 0
    end_node = Node(None, end)
    end.node.g = end.node.h = end.node.f = 0

    open_list = []
    closed_list = []

    open_list.append(start_node)

    while len(open_list) > 0:

        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < index.f:
                current_node = item
                current_index = index

        open_list.pop(current_index)
        closed_list.append(current_node)

        if current_node == end_node:
            path = []
            current = current_node
            while current is not True:
                path.append(current.position)
                current = current.parent
            return path[::-1]

        children = []
        adjanced_squares = [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        
        for new_position in adjanced_squares:
            node_position = new_position