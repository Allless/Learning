def matrixReshape(matrix, r, c):
    size = len(matrix) * len(matrix[0])
    if(size != r*c):
        return matrix
    width = len(matrix[0])
    return [
        [
        matrix[(row * c + col) // width][(row * c + col) % width] 
        for col in range(c)
        ] 
        for row in range(r)
            ]
