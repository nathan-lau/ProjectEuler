print('Problem 7:');

#import math

inputNumber = int(input('Which prime? '))
inputNumber = inputNumber - 2; #adjust the count for arrays
#numberSqrt = math.sqrt(inputNumber)
primeCount = 0;
primeNumber = 3; #starting with the prime 3
primeArray = []
primeArray.append(2); #hardcoding... need to remove
latestPrime = 0; #used to store the last found prime

def checkPrime (number) :
    if number > 1:
        for i in range(2,number):
            if (number % i) == 0:
                primeFlag = 0;
                break
            else:
                primeFlag = 1;
    else:
        primeFlag = 0;
    return(primeFlag);

while primeCount <= inputNumber :
    primeFlag = checkPrime(primeNumber);
    if primeFlag == 1 :
        #primeArray.append(primeNumber)
        latestPrime = primeNumber;
        primeCount = primeCount + 1;
        primeflag = 0;
    primeNumber = primeNumber + 1;

#print(primeArray);
print(latestPrime)
