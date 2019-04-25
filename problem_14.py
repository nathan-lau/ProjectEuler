import math
import time
t = time.time()
print('Problem 14: Longest Collatz Sequence');

#Even numbers
def whenEven(number):
    number = number / 2
    return number

def whenOdd(number):
    number = (number * 3) + 1
    return number

def checkEven(number):
    if number % 2 == 0:
        flag = 1
    else :
        flag = 0
    return flag

startNumber = 13
counter = 1
collatzSequence = []
collatzSequence.append(startNumber)

while startNumber != 1:
    if checkEven(startNumber) == 1:
        nextNumber = whenEven(startNumber)
    else:
        nextNumber = whenOdd(startNumber)
    startNumber = nextNumber
    collatzSequence.append(startNumber)
    counter = counter + 1

print('Chain length is: ', counter)
print(collatzSequence)

elapsed = time.time() - t
print('Processing time: ', elapsed,'seconds')
