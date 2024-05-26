def isPolindrome(number):
    number = str(number)
    for i in range(int(len(number)/2)):
        if number[i] != number[len(number) - i - 1]:
            return False
    return True

def getPolsInRange(start, end):
    return tuple(i for i in range(start, end+1) if isPolindrome(i))
