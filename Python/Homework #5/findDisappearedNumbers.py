def findDissapearedNumbers(array):
    array = set(array)
    return [num for num in range(1, max(array)) if num not in array]