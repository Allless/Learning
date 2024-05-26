def maxPow(number):
    n = 3
    maxValue = 1
    while(maxValue <= number):
        maxValue *= n
    return int(maxValue / n)
