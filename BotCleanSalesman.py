# Создать корень с кратчайшим путём
# Редуцировать матрицу единожды, создать два ответвления по правилам двоичного дерева
# В узле хранить информацию о факте ветвления, выбранный на данный момент путь (Формат?), длину пути, матрицу после /
#  применения редукций всех выбранных путей
# Каждый раз искать в двоичном дереве наименьший неветвящийся узел (берем за переменную корень и спускаемся влево, /
# обновляя переменную каждый раз, когда встречаем неветвящийся узел) (переменная - текущий узел со всеми атрибутами)

# Реализация:

# Класс "узел":
# создаёт узел, который содержит указанную выше информацию

# Класс "решение":
# функция "поиск наименьшего пути", которая будет спускаться влево (если нельзя влево - то вправо) /
# и хранить в переменной подходящие узлы
# функция "вставка узла", которая будет вставлять узел в бинарное дерево по длине выбранного пути
# функция, удаляющая ветвящиеся узлы (кроме корневого (или его тоже?))

# Сторонние функции (или функции класса "решение"):
# Поиск минимумов по строкам и столбцам для редукции (можно написать один, а матрицу транспонировать по необходимости)
# Редукция столбцов и строк (и, может, сразу всей матрицы) (можно использовать именнованные переменные и дефолтный None)
# Нахождние локальной нижней границы обеих ветвей (длины пути)

import numpy as np
import random

# classes
class Node:
    """
    Nodes of graph
    Stores information about brunching, length of way, chosen brunch and matrix in that point
    of solution.
    """
    def __init__(self, lengthOfWay, chosenWay, matrix, brunching=None):
        self.brunching = brunching
        self.length = lengthOfWay
        self.way = chosenWay
        self.matrix = matrix
        self.left = None
        self.right = None

class Solution:
    """
    Creates graph.
    Insert nodes, search minimum length of way and the way.

    Возможно, стоит сохранять в узлах путь к ним, и хранить не в графе, а в бинарном дереве для более простого поиска
    наименьшей длины пути
    """
    rootNode = Node(float('inf'), [], [])

    def insert_node(self, lengthOfWay, chosenWay, matrix, root=rootNode):
        if root is None:
            return Node(lengthOfWay, chosenWay, matrix)
        else:
            if lengthOfWay < root.length:
                root.left = Solution.insert_node(lengthOfWay, chosenWay, matrix, root.left)
            else:
                root.right = Solution.insert_node(lengthOfWay, chosenWay, matrix, root.right)

    def search_shortest(self):
        """Choose shortest and delete from tree"""
        root = Solution.root
        targetNode = None

        if root.left.left is not None:
            targetNode = root.left.left
            root.left.left = None
        elif root.left.left is None and root.left.right is not None:
            targetNode = root.left.right
            root.left.right = root.left.right.right
        elif root.left.left is None and root.left.right is None:
            targetNode = root.left

        return targetNode
#######


# other functions
def printMatrix(matrix):
    print('--------------')
    print(matrix)
    print('--------------')


def min_without(lst, myidx):
    return min(x for idx, x in enumerate(lst) if idx != myidx)


def reduction_of_vectors(matrix):
    min_in_rows = np.amin(matrix, 1)

    for i in range(len(matrix)):
        matrix[:, i] -= min_in_rows

    min_in_cols = np.amin(matrix, 0)
    matrix -= min_in_cols

    return matrix


def root_lower_bound(matrix):
    min_in_rows = np.amin(matrix, 1)

    for i in range(len(matrix)):
        matrix[:, i] -= min_in_rows

    min_in_cols = np.amin(matrix, 0)

    rootLowerBound = sum(min_in_rows) + sum(min_in_cols)

    return rootLowerBound


def zero_sells_estimates(matrix):
    zeroSellsEstimates = np.ones(np.shape(matrix))*float('inf')
    l = len(matrix)
    maxEst = 0
    idxi = 0
    idxj = 0
    for i in range(l):
        for j in range(l):
            if matrix[i][j] == 0:
                zeroSellsEstimates[i][j] = min_without(matrix[i], j) + min_without(matrix[:, j], i)
                if zeroSellsEstimates[i][j] > maxEst:
                    maxEst = zeroSellsEstimates[i][j]
                    idxi = i
                    idxj = j
    print(zeroSellsEstimates)
    return [idxi, idxj], zeroSellsEstimates[idxi, idxj]


def reduction_of_matrix(matrix, indexes):
    idxi, idxj = indexes[0], indexes[1]
    matrix[idxi, :] = float('inf')
    matrix[:, idxj] = float('inf')
    matrix[idxj][idxi] = float('inf')
    return matrix


def matrix_when_chosen_without(matrix, indexes):
    matrix[indexes[0]][indexes[1]] = float('inf')
    return matix


def lower_bound_of_brunches(MaxEstimate, lowerBoundOfParent):
    return MaxEstimate + lowerBoundOfParent
#######


# body ###
########
np.random.seed(5)
# preparation #

# manipulation with matrix
startMatrix = np.random.uniform(0, 25, (5, 5)).round(0)
np.array(startMatrix)

printMatrix(startMatrix)

###

currentMatrix = startMatrix


MatrixIsEmpty = False
way = []

# 0. finding the root lower bound
rootLowerBound = root_lower_bound(currentMatrix)
virtualLowerBoundWith = rootLowerBound
virtualLowerBoundWithout = rootLowerBound

while not MatrixIsEmpty:
    # 1. reduction of rows and columns
    currentMatrix = reduction_of_vectors(currentMatrix)
    printMatrix(currentMatrix)

    # 2. calculation of zero sells estimates
    sellWithMaxEstimate, MaxEstimate = zero_sells_estimates(currentMatrix)
    printMatrix(currentMatrix)
    # 3. calculation of branches' lower bounds
    virtualCurrentMatrix = currentMatrix

    virtualCurrentMatrix = reduction_of_matrix(virtualCurrentMatrix, sellWithMaxEstimate)
    print('virtual')
    printMatrix(virtualCurrentMatrix)
    localLowerBound = root_lower_bound(virtualCurrentMatrix)

    virtualLowerBoundWith = lower_bound_of_brunches(localLowerBound, virtualLowerBoundWith)
    virtualLowerBoundWithout = lower_bound_of_brunches(MaxEstimate, virtualLowerBoundWithout)

    # 4. choosing of brunch
    if virtualLowerBoundWith <= virtualLowerBoundWithout:
        print('before')
        printMatrix(currentMatrix)
        currentMatrix[:, :] = virtualCurrentMatrix[:, :]
        print('after')
        printMatrix(currentMatrix)
        way.append([sellWithMaxEstimate[0], sellWithMaxEstimate[0]])
    else:
        print('else')
        printMatrix(currentMatrix)
        currentMatrix[sellWithMaxEstimate[0], sellWithMaxEstimate[1]] = 100000000
        print('else')
        printMatrix(currentMatrix)

    if np.amin(currentMatrix) > 10000:
        print(way)
        MatrixIsEmpty = True


#######
