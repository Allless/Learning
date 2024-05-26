def getNumberRoot(number):
    while (number > 9):
        number = sum(map(int, str(number)))
    return number
