import math
import time
t = time.time()
print('Problem 16: Power Digit Sum');

power = int(input('Enter the power: '))

def twoPower(power):
    i = 0
    answer = 1
    while i < power:
        answer = answer * 2
        i+=1
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

answer = twoPower(power)
sum = sumDigits(answer)
print('Answer: ', sum)

elapsed = time.time() - t
print('Processing time: ', elapsed,'seconds')
