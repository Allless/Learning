def getSuffixSums(*numbers):
    return [sum(numbers[i:]) for i in range(len(numbers))]