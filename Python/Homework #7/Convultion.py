# I hope that i got the task correctly
def mul(first, second):
    mySum = sum([sum([first[i][j] * second[i][j] for j in range(len(first))]) for i in range(len(first))])
    return mySum

def getConvolutionMatrix(firstMatrix, secMatrix):
    result = []
    for i in range(0, len(firstMatrix) - len(secMatrix) + 1):
        row = []
        for j in range(0, len(firstMatrix) - len(secMatrix) + 1):
            croppedMatrix = []
            for k in range(0,len(secMatrix)):
                croppedRow = []
                for l in range(0,len(secMatrix)):
                    croppedRow.append(firstMatrix[i+k][j+l])
                croppedMatrix.append(croppedRow)
                croppedRow = []
            sum = mul(croppedMatrix, secMatrix)
            row.append(sum)
        result.append(row)
        row = []
            
    return result

print(getConvolutionMatrix(
    [[0,1,1,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,0,0,1,1,1,0],
    [0,0,0,1,1,0,0],
    [0,0,1,1,0,0,0],
    [0,1,1,0,0,0,0],
    [1,1,0,0,0,0,0]],
    [[1,0,1],
    [0,1,0],
    [1,0,1]]
))