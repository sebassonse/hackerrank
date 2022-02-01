#!/usr/bin/python

# Head ends here
import numpy as np


def closest_neighbors(neighbors):
    res = 0
    how_many = 0
    for each in neighbors.values():
        res += each
        how_many += 1
    average = res/how_many
    closestNeighbors = {}
    for key, each in neighbors.items():
        if each <= average:
            closestNeighbors[key] = each
    return closestNeighbors


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

        # keep just closest

        """if len(nodes) > 5:
            graph[i] = closest_neighbors(graph[i])"""

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


def next_move(way, nodes):
    posx, posy = (0, 0)
    k = 0
    while k != len(way)-1:
        if posx < nodes[way[k+1]][1]:
            print('RIGHT')
            posx += 1
        elif posx > nodes[way[k+1]][1]:
            print('LEFT')
            posx -= 1
        elif posy < nodes[way[k+1]][0]:
            print("DOWN")
            posy += 1
        elif posy > nodes[way[k+1]][0]:
            print("UP")
            posy -= 1
        elif [posy, posx] == nodes[way[k+1]]:
            print("CLEAN")
            k += 1
        try:
            position = [int(i) for i in input().strip().split()]
            boards = [[j for j in input().strip()] for i in range(5)]
        except EOFError:
            continue


# Tail starts here


pos = [int(i) for i in input().strip().split()]
board = [[j for j in input().strip()] for i in range(5)]

# START OF MY CODE
nodes = preparation(pos[0], pos[1], board)
graph = graphRender(nodes)
way = all_way(graph)
next_move(way, nodes)


