import math
import time

t = time.time()
print('Problem 21: Amicable Numbers');

#Let d(n) be defined as the number of proper divisors of n (numbers less than n which devide even ly into n). If d(a) = b and d(b) = a, where a does not equal b, then a and b are an imicable pair adn each of a and b are called amicable numbers.

#For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71, and 142; so d(284) = 220.

#Evaluate the sum of all the amicable numbers under 10,000.

def findFactors(number): #fucnction to find all the factors of the input. Does not incldue input
    factors = []
    i = 1
    while i < number:
        if number % i == 0:
            factors.append(i)
            i+=1
        else:
            i+=1
    return factors

def sumArray(factors): #only works if the numbers are stored in an array
    i = 0
    sum = 0
    while i < len(factors):
        sum = sum + factors[i]
        i = i + 1
    return sum

def amicableNum(number):
    amicablePair = []
    flag = 0;
    factorA = findFactors(number)
    sumA = sumArray(factorA)
    factorB = findFactors(sumA)
    sumB = sumArray(factorB)
    if number == sumB:
        if number != sumA: #need to make sure A does not equal B
            flag = 1;
    return flag;


max = int(input('Enter the max value: '))
i = 1
amicableArray = []
while i <= max:
    if amicableNum(i) == 1:
        amicableArray.append(i)
        i += 1
    else:
        i += 1

print(amicableArray)
print(sumArray(amicableArray))


elapsed = time.time() - t
print('Processing time: ', elapsed,'seconds')
