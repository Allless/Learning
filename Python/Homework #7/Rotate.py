def rotate(matrix):
    for i in range(len(matrix)//2):
        for j in range(i, len(matrix) - i - 1):
            x = i
            y = j
            temp = matrix[x][y]
            for k in range(3):
                matrix [x][y] = matrix[len(matrix) - y - 1][x]
                x, y = len(matrix) - y - 1, x
            matrix[x][y] = temp

    return matrix

print(rotate([
    [5,1,9,11],
    [2,4,8,10],
    [13,3,6,7],
    [15,14,12,16],
]), rotate([
    [1,2,3],
    [4,5,6],
    [7,8,9]
]))
            