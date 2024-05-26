def getCycleShift(n,k, *numbers):
    return numbers[len(numbers) - k:] + numbers[:len(numbers) - k]
