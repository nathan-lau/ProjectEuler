import math
import time
t = time.time()
print('Problem 12: Highly divisible triangle number');

#inputNumber = int(input('Enter the nth triangle number: '))

def triangleNumber (number):
    i = 1
    sum = 0
    while i <= number:
        sum = sum + i
        i = i + 1
    return sum

def numberOfDivisors (number):
    i = 1
    sqrt = math.sqrt(number)
    answer = 0
    while i < number :
        if number % i == 0 :
            answer = answer + 1
            i = i + 1
        else :
            i = i + 1
    return answer

#triangle = triangleNumber(inputNumber)
#answer = numberOfDivisors(triangle)
#print('The triangle number is: ', triangle)
#print(triangle, ' has ', answer, ' divisors')

inputNumber = int(input('Over how many divisors: '))
i = 1
answer = 0

while answer < inputNumber :
    triangle = triangleNumber(i)
    answer = numberOfDivisors(triangle)
    i = i + 1
print('The triangle number is: ', triangle)
print('It has ', answer, 'divisors')

elapsed = time.time() - t
print('Processing time: ', round(elapsed,2),'seconds')
