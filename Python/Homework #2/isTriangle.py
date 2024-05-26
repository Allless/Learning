def isTriangle(a,b,c):
    m = max(a,b,c)
    if a + b + c - m > m:
        return True
    return False
