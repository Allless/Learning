def numDigsProd(number):
    res = 1
    for n in str(number):
        if n != '0':
            res *= int(n)
    return res
