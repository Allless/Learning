def getquadSol(a,b,c):
    result1 = ''
    result2 = ''
    disc = ''
    isQuadric = 'Quadratic equation'
    if (a == 0):
        isQuadric = 'Non-quadratic equation'
        if(c == 0):
            if(b == 0):
                hasSolution = 'Infinite solutions'
            else:
                hasSolution = 'One Solution:'
                result1 = 0
        else:
            if(b == 0):
                hasSolution = 'No Solutions'
            else:
                hasSolution = 'One Solution:'
                result1 = -c/b
    else:
        d = b*b - 4*a*c
        if d > 0:
            hasSolution = 'Two solutions:'
            result1 = (-b + d**0.5)/(2*a)
            result2 = (-b - d**0.5)/(2*a)
        elif d == 0:
            hasSolution = 'One Solution:'
            result1 = -b/(2*a)
        else:
            hasSolution = 'No Solutions'
        disc = f'\n Discriminant: {d}'

    return f'''{isQuadric}{disc}
{hasSolution} {result1} {result2}'''

