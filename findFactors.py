import math
import time

t = time.time()
print('Problem 21: Amicable Numbers');

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


number = int(input('Enter the number: '))
answer = findFactors(number)

print(answer)


elapsed = time.time() - t
print('Processing time: ', elapsed,'seconds')
