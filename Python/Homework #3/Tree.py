def getTree(width):
    heigh = int(width/2 +1)
    return '\n'.join([' ' * (heigh - i) + ('*' * (2 * i - 1)) + ' ' * (heigh - i) for i in range(1, heigh + 1)])
