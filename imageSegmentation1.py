matrix = []
for n in range(4):
    inp = str(input()).strip(' ')
    new_row = []
    for i in range(len(inp)):
        new_row.append(int(inp[i]))
    matrix.append(new_row)

print(matrix)

(I, J) = (len(matrix), len(matrix[0]))

# buffers for except "index out of range"
matrix.insert(0, [i*0 for i in range(len(matrix[0]))])
matrix.insert(len(matrix), [i*0 for i in range(len(matrix[0]))])
for i in range(len(matrix)):
    matrix[i].insert(len(matrix[0]), int(0))
    matrix[i].insert(0, int(0))

print(matrix)
numOfClusters = 0

for i in range(1, I+1):
    for j in range(1, J+1):
        if matrix[i][j] == 0:
            continue
        if matrix[i][j] == 1 and matrix[i][j+1] != 2:
            numOfClusters += 1
        elif matrix[i][j] == 2 and matrix[i][j+1] == 2 and matrix[i-1][j] != 2:
            numOfClusters -= 1
        matrix[i][j] = 2
        matrix[i][j+1] = int(matrix[i][j+1] != 0)*2
        matrix[i][j-1] = int(matrix[i][j-1] != 0)*2
        matrix[i+1][j] = int(matrix[i+1][j] != 0)*2
        matrix[i-1][j] = int(matrix[i-1][j] != 0)*2
        print(numOfClusters)


print('final number of clusters ', numOfClusters)
