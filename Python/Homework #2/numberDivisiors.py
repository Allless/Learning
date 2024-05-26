def getNumDivs(number):
    count = 0
    for i in range(1, int(number**0.5)):
        if(number%i == 0):
            count += 1
    count *= 2
    if(int(number**0.5) == number**0.5):
        count += 1
    return count