print('Problem 10:');

inputNumber = int(input('Prime numbers below...? '))

def sumPrimes(max):
    sum = 0 #initiate sum as 0
    sieve = [True] * max #create inital array the size of max

    for p in range(2, max):
        if sieve[p]: #For the elements that are true...
            sum = sum + p
            for i in range(p*p, max, p): #starting from the square of p going to max incrementing by p
                sieve[i] = False
    return sum

print ('Sum of primes below ', inputNumber, ' is equal to ', sumPrimes(inputNumber))
