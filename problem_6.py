print('Problem 6:');

number = int(input('Enter Number: '))
sumOfSquares = 0 ;
sumCount = number;
squareOfSums = 0;
squareCount = number;
answer = 0;

while sumCount > 0:
    sumOfSquares = sumOfSquares + (sumCount * sumCount);
    sumCount = sumCount - 1;

while squareCount > 0:
    squareOfSums = squareOfSums + squareCount;
    squareCount = squareCount - 1;
squareOfSums = squareOfSums * squareOfSums;

answer = squareOfSums - sumOfSquares;

print(sumOfSquares);
print(squareOfSums);
print(answer);
