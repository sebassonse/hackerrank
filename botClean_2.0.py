def graphRender(nodes):
    # find the closest dirty places to bot and each other
    graph = dict()

    for i in range(len(nodes)):
        graph[i] = dict()

        for j in range(len(nodes)):
            if i == j or j == 0:
                continue
            else:
                # find all neighbors
                graph[i][j] = (abs(nodes[i][0] - nodes[j][0]) + abs(nodes[i][1] - nodes[j][1]))

    return graph


def preparation(posr, posc, board):

    # dict with placements of all nodes (bot + dirty cells)
    q = len(board)

    nodes = dict()
    nodes[0] = [posr, posc]
    numOfEl = 1

    # find dirty places
    for row in range(q):
        for col in range(q):
            if board[row][col] == 'd':
                nodes[numOfEl] = [row, col]
                numOfEl += 1
    return nodes


def all_way(graph):
    size = len(graph)
    way = [0]
    while len(way) != size:
        next = min(graph[way[-1]], key=graph[way[-1]].get)
        for subdict in graph.values():
            subdict[next] = 1000
        way.append(next)
    return way


def next_move(posx, posy, way, nodes):
    if posx < nodes[way[0]][1]:
        print('RIGHT')
        posx += 1
    elif posx > nodes[way[0]][1]:
        print('LEFT')
        posx -= 1
    elif posy < nodes[way[0]][0]:
        print("DOWN")
        posy += 1
    elif posy > nodes[way[0]][0]:
        print("UP")
        posy -= 1
    elif [posy, posx] == nodes[way[0]]:
        print("CLEAN")


def next_move_2(posy, posx, graph, nodes):

    nextNode = min(graph[0], key=graph[0].get)
    coordsOfNextNode = nodes[nextNode]

    if posx < coordsOfNextNode[1]:
        print('RIGHT')
    elif posx > coordsOfNextNode[1]:
        print('LEFT')
    elif posy < coordsOfNextNode[0]:
        print("DOWN")
    elif posy > coordsOfNextNode[0]:
        print("UP")
    elif [posy, posx] == coordsOfNextNode:
        print("CLEAN")
# Tail starts here


pos = [int(i) for i in input().strip().split()]
board = [[j for j in input().strip()] for i in range(5)]

# START OF MY CODE
nodes = preparation(pos[0], pos[1], board)
graph = graphRender(nodes)
next_move_2(pos[0], pos[1], graph, nodes)

