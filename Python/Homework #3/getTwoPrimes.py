def isPrime(number):
    for i in range(2, int(number**0.5) +1):
        if(number%i == 0):
            return False
    return True

def getTwoPrimes(number):
    for i in range(2, int(number/2) +1):
        if isPrime(i) and isPrime(number - i):
            return i, number-i