import math
import time

t = time.time()
print('Problem 20: Factorial Digit Sum');

def factorial(number):
    i = 1;
    answer = 1;
    while i <= number:
        answer = answer * i
        #print(answer)
        i += 1
    return answer

def sumDigits(number):
    numArray = []
    while number >= 1:
        digit = number % 10
        number = number / 10
        numArray.append(digit)
    i = 0
    sum = 0
    while i < len(numArray):
        sum = sum + numArray[i]
        i = i + 1
    return sum

number = int(input('Enter the factorial: '))
answer = factorial(number)
sum = sumDigits(answer)
print(sum)


elapsed = time.time() - t
print('Processing time: ', elapsed,'seconds')
