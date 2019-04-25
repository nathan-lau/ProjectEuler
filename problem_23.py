import math
import time
import csv

t = time.time()
print('Problem 23: Non-abundant sums');

#A perfect number is a number for which the sums of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

#A number n is called deficient if the number of its proper divisors is less than n and it is called abundant if this sum exceeds n.

#As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers.

#However, this upper limit cannot bre expressed as the sum of two abundant numbers isless than this limit.

#Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers

def findFactors(number):
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

def perfectNumber(number):
    flag = 0
    factors = findFactors(number)
    sum = sumArray(factors)
    if number == sum:
        flag = 1
    if number < sum: #Abundant number
        flag = 2
    if number > sum: #Deficient number
        flag = 3
    return flag

perfectNumbers = []
abundantNumbers = []
deficientNumbers = []

number = int(input('Enter numbrer: '))
i = 1
while i <= number:
    if perfectNumber(i) == 1:
        perfectNumbers.append(i)
    if perfectNumber(i) == 2:
        abundantNumbers.append(i)
    if perfectNumber(i) == 3:
        deficientNumbers.append(i)
    i += 1;

print('Perfect Numbers: ', perfectNumbers)
print('Abundant Numbers: ', abundantNumbers)
print('Deficient Numbers: ', deficientNumbers)



elapsed = time.time() - t
print('Processing time: ', elapsed,'seconds')
