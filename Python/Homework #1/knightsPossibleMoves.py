def knightsPossibleMoves(x,y):
    res = []
    for i in (-1,1):
        for j in (-2,2):
            res += [(x+i,y+j),(x+j,y+i)]
    return res
print(knightsPossibleMoves(6,4))