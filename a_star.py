class Node():

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position


def astar_calculate(maze_val, start_val, end_val):
    start_node = Node(None, start_val)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end_val)
    end_node.g = end_node.h = end_node.f = 0

    open_list = []
    closed_list = []

    open_list.append(start_node)

    while len(open_list) > 0:

        curr_node = open_list[0]
        curr_idx = 0

        for index, item in enumerate(open_list):
            if item.f < curr_node.f:
                curr_node = item
                curr_idx = index

        open_list.pop(curr_idx)
        closed_list.append(curr_node)

        if curr_node == end_node:
            path = []
            current = curr_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1]

        children = []
        for new_pos in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:

            node_pos = (curr_node.position[0] + new_pos[0], curr_node.position[1] + new_pos[1])

            if node_pos[0] > (len(maze_val) - 1) or node_pos[0] < 0 or node_pos[1] > (
                    len(maze_val[len(maze_val) - 1]) - 1) or node_pos[1] < 0:
                continue

            if maze_val[node_pos[0]][node_pos[1]] != 0:
                continue

            new_node = Node(curr_node, node_pos)

            children.append(new_node)

        for child in children:

            for closed_child in closed_list:
                if child == closed_child:
                    continue

            child.g = curr_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + (
                        (child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            open_list.append(child)



    maze = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    start = (0, 0)
    end = (7, 6)

    path = astar_calculate(maze, start, end)
    print(path)