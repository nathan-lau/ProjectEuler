import time

t = time.time()
print('Problem 10:');

primeNumber = 3;
primeSum = 2;
#primeArray = [];
#primeArray.append(2);

inputNumber = int(input('Prime numbers below...? '))

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

while primeNumber <= inputNumber :
    if (checkPrime(primeNumber) == 1) :
        print(primeNumber)
        primeSum = primeSum + primeNumber;
        #primeArray.append(primeNumber);
    primeNumber =primeNumber + 1;


#print(primeArray)
print('Sum of primes less than ', inputNumber, ' is ',primeSum,'.')
elapsed = time.time() - t
print('Processing time: ', round(elapsed,2),'seconds')
